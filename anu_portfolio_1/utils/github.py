from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Iterable
from urllib.parse import quote

import pandas as pd
import requests
import streamlit as st

from utils.data import featured_repo_names
from utils.text import safe_int

GITHUB_USERNAME = "anu-2024"
GITHUB_API = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
GITHUB_PROFILE = f"https://github.com/{GITHUB_USERNAME}"
REQUEST_TIMEOUT = 12
CACHE_TTL_SECONDS = 600


@dataclass(frozen=True)
class GitHubSnapshot:
    repos: list[dict[str, Any]]
    fetched_at: str | None
    error: str | None


def _github_token() -> str:
    try:
        return str(st.secrets.get("GITHUB_TOKEN", "") or "").strip()
    except Exception:
        return ""


def _headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Anu-A-Portfolio",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = _github_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _friendly_error(exc: Exception) -> str:
    if isinstance(exc, requests.HTTPError) and exc.response is not None:
        status = exc.response.status_code
        remaining = exc.response.headers.get("X-RateLimit-Remaining", "")
        if status == 403 and remaining == "0":
            return (
                "GitHub API rate limit reached. The page will recover after the limit resets, "
                "or you can add a GITHUB_TOKEN secret for a higher limit."
            )
        if status == 404:
            return "The GitHub profile was not found. Check the configured username."
        if status == 401:
            return "GitHub authentication failed. Check the GITHUB_TOKEN secret."
        return f"GitHub returned status {status}. Live repository data is temporarily unavailable."
    if isinstance(exc, requests.Timeout):
        return "GitHub took too long to respond. Live repository data will refresh on the next load."
    if isinstance(exc, requests.RequestException):
        return "Could not reach GitHub. Live repository data will refresh on the next load."
    return "Live GitHub data is temporarily unavailable. The curated project showcase remains available."


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def fetch_github_repos() -> GitHubSnapshot:
    repos: list[dict[str, Any]] = []
    try:
        with requests.Session() as session:
            for page in range(1, 4):
                response = session.get(
                    GITHUB_API,
                    params={
                        "sort": "updated",
                        "per_page": 100,
                        "type": "owner",
                        "page": page,
                    },
                    headers=_headers(),
                    timeout=REQUEST_TIMEOUT,
                )
                response.raise_for_status()
                batch = response.json()
                if not isinstance(batch, list):
                    raise ValueError("Unexpected GitHub response format.")
                repos.extend(batch)
                if len(batch) < 100:
                    break
    except Exception as exc:
        return GitHubSnapshot(repos=[], fetched_at=None, error=_friendly_error(exc))

    visible = [
        repo
        for repo in repos
        if isinstance(repo, dict) and not repo.get("fork") and not repo.get("private")
    ]
    visible.sort(key=lambda repo: repo.get("updated_at") or "", reverse=True)
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return GitHubSnapshot(repos=visible, fetched_at=fetched_at, error=None)


@st.cache_data(ttl=CACHE_TTL_SECONDS, show_spinner=False)
def fetch_repo_languages(full_name: str) -> dict[str, int]:
    if not full_name:
        return {}
    url = f"https://api.github.com/repos/{quote(full_name, safe='/')}/languages"
    try:
        response = requests.get(url, headers=_headers(), timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            return {}
        return {str(name): safe_int(value) for name, value in payload.items()}
    except Exception:
        return {}


def clear_github_cache() -> None:
    fetch_github_repos.clear()
    fetch_repo_languages.clear()


def find_repo(repos: Iterable[dict[str, Any]], repo_name: str) -> dict[str, Any] | None:
    target = (repo_name or "").lower()
    for repo in repos:
        if str(repo.get("name") or "").lower() == target:
            return repo
    return None


def featured_repos(repos: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    names = {name.lower() for name in featured_repo_names()}
    return [repo for repo in repos if str(repo.get("name") or "").lower() in names]


def other_repos(repos: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    names = {name.lower() for name in featured_repo_names()}
    return [repo for repo in repos if str(repo.get("name") or "").lower() not in names]


def repo_stats(repos: Iterable[dict[str, Any]]) -> dict[str, int]:
    repo_list = list(repos)
    languages = {repo.get("language") for repo in repo_list if repo.get("language")}
    return {
        "repositories": len(repo_list),
        "stars": sum(safe_int(repo.get("stargazers_count")) for repo in repo_list),
        "forks": sum(safe_int(repo.get("forks_count")) for repo in repo_list),
        "languages": len(languages),
    }


def language_mix(repos: Iterable[dict[str, Any]], limit: int = 7) -> list[dict[str, Any]]:
    repo_list = list(repos)
    if not repo_list:
        return []
    frame = pd.DataFrame(
        {"language": [repo.get("language") or "Not specified" for repo in repo_list]}
    )
    counts = frame["language"].value_counts().head(limit)
    total = int(counts.sum())
    if total <= 0:
        return []
    return [
        {
            "language": str(language),
            "count": int(count),
            "percent": round(int(count) / total * 100, 1),
        }
        for language, count in counts.items()
    ]


def repo_language_breakdown(full_name: str, limit: int = 5) -> list[dict[str, Any]]:
    languages = fetch_repo_languages(full_name)
    total = sum(languages.values())
    if total <= 0:
        return []
    ordered = sorted(languages.items(), key=lambda item: item[1], reverse=True)[:limit]
    return [
        {"language": name, "percent": round(value / total * 100, 1)}
        for name, value in ordered
    ]
