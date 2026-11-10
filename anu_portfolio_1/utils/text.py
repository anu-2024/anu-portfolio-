import html
import re
from datetime import datetime
from typing import Any, Iterable

FALLBACK_ANSWER = (
    "I can help with questions about Anu's projects, skills, experience, education, "
    "certifications, GitHub or contact details. Try asking about Generative AI projects, "
    "Python skills or internship experience."
)


def escape(value: Any) -> str:
    return html.escape(str(value), quote=True)


def truncate(value: Any, limit: int = 180) -> str:
    text = str(value or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def format_date(value: str | None) -> str:
    if not value:
        return "Not available"
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.strftime("%d %b %Y")
    except ValueError:
        return str(value)[:10]


def format_datetime(value: str | None) -> str:
    if not value:
        return "Not available"
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.strftime("%d %b %Y, %H:%M UTC")
    except ValueError:
        return str(value)


def format_number(value: Any) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "0"


def safe_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def initials(value: str, fallback: str = "AA") -> str:
    parts = [part for part in str(value or "").split() if part]
    if not parts:
        return fallback
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    return singular if count == 1 else (plural or singular + "s")


def _normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def answer_question(question: str, entries: Iterable[dict[str, Any]]) -> tuple[str, str | None]:
    normalized = _normalized(question)
    if not normalized:
        return FALLBACK_ANSWER, None

    best_answer = FALLBACK_ANSWER
    best_id: str | None = None
    best_score = 0

    for entry in entries:
        score = 0
        for keyword in entry.get("keywords", []):
            key = _normalized(keyword)
            if key and key in normalized:
                score += max(1, len(key.split()))
        if normalized == _normalized(entry.get("question", "")):
            score += 5
        if score > best_score:
            best_score = score
            best_answer = str(entry.get("answer", FALLBACK_ANSWER))
            best_id = str(entry.get("id", "")) or None

    return best_answer, best_id


def suggested_questions(entries: Iterable[dict[str, Any]], limit: int = 6) -> list[dict[str, str]]:
    preferred = (
        "generative-ai",
        "python",
        "experience",
        "education",
        "availability",
        "contact",
        "github",
        "resume",
    )
    entries = list(entries)
    selected = [
        entry
        for preferred_id in preferred
        for entry in entries
        if str(entry.get("id", "")) == preferred_id
    ]
    if len(selected) < limit:
        seen = {str(entry.get("id", "")) for entry in selected}
        for entry in entries:
            entry_id = str(entry.get("id", ""))
            if entry_id not in seen:
                selected.append(entry)
                seen.add(entry_id)
            if len(selected) >= limit:
                break
    return [
        {"id": str(entry.get("id", "")), "question": str(entry.get("question", ""))}
        for entry in selected[:limit]
    ]
