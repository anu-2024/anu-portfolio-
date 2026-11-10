import streamlit as st

from components.ui import section_header
from utils.data import load_profile
from utils.text import escape


def render_education() -> None:
    profile = load_profile()
    cards = "".join(
        f"""
        <div class="panel education-card">
          <span class="year">{escape(item["period"])}</span>
          <h3>{escape(item["degree"])}</h3>
          <div class="institution">{escape(item["institution"])}</div>
          <div class="location">{escape(item["location"])}</div>
          <p class="note">{escape(item["note"])}</p>
        </div>
        """
        for item in profile["education"]
    )

    section_header(
        "education",
        "05",
        "Education",
        "A foundation in computer applications.",
        "Formal study in computer science, programming and applied AI, alongside project-based learning.",
    )

    st.markdown(
        f'<div class="education-grid">{cards}</div>',
        unsafe_allow_html=True,
    )
