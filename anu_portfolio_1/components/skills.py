import streamlit as st

from components.ui import chip_list, icon_svg, section_header
from utils.data import load_skills, project_map
from utils.text import escape


def render_skills() -> None:
    skills = load_skills()
    projects = project_map()

    section_header(
        "skills",
        "02",
        "Technical skills",
        "A toolkit shaped by hands-on work.",
        "Languages, AI tooling, data workflows and the web tools used across the featured projects.",
    )

    cards = []
    for skill in skills:
        related = " · ".join(
            f'<a href="#detail-{escape(slug)}">{escape(projects[slug]["title"])}</a>'
            for slug in skill.get("projects", [])
            if slug in projects
        )
        cards.append(
            f"""
            <div class="panel skill-card">
              <div class="skill-icon">{icon_svg(escape(skill["icon"]))}</div>
              <h3>{escape(skill["name"])}</h3>
              <p>{escape(skill["description"])}</p>
              <div class="chips">{chip_list(skill["items"])}</div>
              <div class="skill-related">Used in {related}</div>
            </div>
            """
        )

    st.markdown(
        f'<div class="skill-grid">{"".join(cards)}</div>',
        unsafe_allow_html=True,
    )
