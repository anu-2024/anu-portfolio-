import streamlit as st

from utils.text import escape

ICONS = {
    "code": '<path d="m8 9-3 3 3 3"/><path d="m16 9 3 3-3 3"/><path d="m14 6-4 12"/>',
    "spark": '<path d="M12 3v3"/><path d="M12 18v3"/><path d="M3 12h3"/><path d="M18 12h3"/><path d="m5.6 5.6 2.1 2.1"/><path d="m16.3 16.3 2.1 2.1"/><path d="m18.4 5.6-2.1 2.1"/><path d="m7.7 16.3-2.1 2.1"/><circle cx="12" cy="12" r="3"/>',
    "chart": '<path d="M4 19V5"/><path d="M4 19h16"/><path d="m7 15 3-4 3 2 4-6"/>',
    "globe": '<circle cx="12" cy="12" r="8"/><path d="M4 12h16"/><path d="M12 4a13 13 0 0 1 0 16"/><path d="M12 4a13 13 0 0 0 0 16"/>',
    "database": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "external": '<path d="M14 5h5v5"/><path d="m10 14 9-9"/><path d="M19 14v4a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h4"/>',
}


def section_header(
    anchor_id: str,
    number: str,
    label: str,
    title: str,
    subtitle: str = "",
    compact: bool = False,
) -> None:
    subtitle_html = f"<p>{escape(subtitle)}</p>" if subtitle else ""
    extra_class = " compact" if compact else ""
    st.markdown(
        f"""
        <div id="{escape(anchor_id)}" class="anchor"></div>
        <div class="section-head{extra_class}">
          <div>
            <span class="eyebrow">{escape(number)} — {escape(label)}</span>
            <h2>{escape(title)}</h2>
          </div>
          {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def icon_svg(name: str, size: int = 20) -> str:
    body = ICONS.get(name, ICONS["spark"])
    return (
        f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
        f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{body}</svg>'
    )


def chip_list(items: list[str]) -> str:
    return "".join(f'<span class="chip">{escape(item)}</span>' for item in items)
