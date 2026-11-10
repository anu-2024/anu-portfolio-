import streamlit as st

from utils.assets import resume_available, resume_data_uri
from utils.data import load_profile
from utils.text import escape


def render_navigation(theme: str) -> None:
    profile = load_profile()
    name = escape(profile["name"])
    initials = escape(profile["initials"])
    target_theme = "light" if theme == "dark" else "dark"
    theme_icon = "☀" if theme == "dark" else "☾"
    theme_label = "Light" if theme == "dark" else "Dark"
    resume_href = resume_data_uri() if resume_available() else "#recruiter"
    resume_attrs = ' download="Anu_A_Resume.pdf"' if resume_available() else ""

    links = [
        ("Home", "#home"),
        ("About", "#about"),
        ("Skills", "#skills"),
        ("Projects", "#projects"),
        ("Experience", "#experience"),
        ("Certifications", "#certifications"),
        ("Leadership", "#leadership"),
        ("GitHub", "#github"),
        ("Contact", "#contact"),
    ]
    nav_links = "".join(
        f'<a href="{href}">{escape(label)}</a>' for label, href in links
    )

    st.markdown(
        f"""
        <div class="topbar">
          <a class="brand" href="#home" aria-label="{name} home">
            <span class="brand-mark">{initials}</span>
            <span>{name}<small> / portfolio</small></span>
          </a>
          <nav class="nav-links" aria-label="Primary navigation">
            {nav_links}
          </nav>
          <div class="nav-utils">
            <a class="nav-pill" href="?theme={target_theme}" title="Switch to {theme_label.lower()} mode">
              {theme_icon} {theme_label}
            </a>
            <a class="nav-pill primary" href="{resume_href}"{resume_attrs}>Resume ↓</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
