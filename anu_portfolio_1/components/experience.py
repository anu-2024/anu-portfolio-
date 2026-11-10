import streamlit as st

from components.ui import chip_list, section_header
from utils.data import load_profile
from utils.text import escape


def render_experience() -> None:
    profile = load_profile()
    items = []
    for item in profile["experience"]:
        items.append(
            f"""
            <div class="timeline-item">
              <div class="timeline-meta">{escape(item["period"])} · {escape(item["location"])}</div>
              <h3>{escape(item["role"])}</h3>
              <div class="timeline-org">{escape(item["organization"])}</div>
              <p>{escape(item["summary"])}</p>
              <div class="chips">{chip_list(item["tags"])}</div>
            </div>
            """
        )

    section_header(
        "experience",
        "04",
        "Experience",
        "Learning by building and teaching.",
        "Internships, instruction and hands-on project work across AI, data and software.",
    )

    st.markdown(
        f"""
        <div class="panel">
          <div class="timeline">{''.join(items)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
