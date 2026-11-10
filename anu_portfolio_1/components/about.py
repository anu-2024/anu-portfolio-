import streamlit as st

from components.ui import section_header
from utils.data import load_profile
from utils.text import escape


def render_about() -> None:
    profile = load_profile()
    paragraphs = "".join(
        f"<p>{escape(paragraph)}</p>" for paragraph in profile["about_paragraphs"]
    )
    focus = "".join(
        f'<li><span class="num">{index:02d}</span><span>{escape(item)}</span></li>'
        for index, item in enumerate(profile["focus"], start=1)
    )
    education = profile["education"][0]

    section_header(
        "about",
        "01",
        "About",
        "Curious by nature. Practical by design.",
        "A computer applications student building at the intersection of AI, software engineering and data.",
    )

    st.markdown(
        f"""
        <div class="about-grid">
          <div class="panel about-copy">
            {paragraphs}
          </div>
          <div class="panel">
            <span class="eyebrow">Current focus</span>
            <h3 style="margin:0.4rem 0 1rem;font-size:1.1rem;">From prototype to useful product</h3>
            <ul class="focus-list">{focus}</ul>
            <div class="mini-education">
              <span class="eyebrow">Currently studying</span>
              <strong>{escape(education["degree"])} · {escape(education["institution"])}</strong>
              <span>{escape(education["period"])} · {escape(education["location"])}</span>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
