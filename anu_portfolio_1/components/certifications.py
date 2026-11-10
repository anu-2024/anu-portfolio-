import streamlit as st

from components.ui import section_header
from utils.data import load_profile
from utils.text import escape, initials


def render_certifications() -> None:
    profile = load_profile()
    cards = []
    for item in profile["certifications"]:
        provider = item["provider"]
        badge = provider.upper() if len(provider) <= 3 else initials(provider, provider[:2])
        cards.append(
            f"""
            <div class="panel cert-card">
              <div class="cert-badge">{escape(badge)}</div>
              <div>
                <h3>{escape(item["title"])}</h3>
                <p>{escape(provider)}</p>
              </div>
            </div>
            """
        )

    section_header(
        "certifications",
        "06",
        "Certifications",
        "Structured learning, applied to projects.",
        "Courses and learning programs across AI agents, data, front-end development, design and computer science fundamentals.",
    )

    st.markdown(
        f'<div class="cert-grid">{"".join(cards)}</div>',
        unsafe_allow_html=True,
    )
