import streamlit as st

from utils.assets import image_data_uri, resume_available, resume_data_uri
from utils.data import load_profile, load_projects
from utils.text import escape

MARQUEE_ITEMS = [
    "Python",
    "Generative AI",
    "Machine Learning",
    "Streamlit",
    "FastAPI",
    "Pandas",
    "Scikit-learn",
    "APIs",
    "SQL",
    "Docker",
    "GitHub",
    "Data Visualisation",
]


def _marquee_group() -> str:
    items = "".join(
        f'<span class="marquee-item">{escape(item)}</span><span class="marquee-dot">✦</span>'
        for item in MARQUEE_ITEMS
    )
    return f'<div class="marquee-group">{items}</div>'


def render_hero() -> None:
    profile = load_profile()
    projects = load_projects()
    name = escape(profile["name"])
    image_uri = image_data_uri()
    resume_href = resume_data_uri() if resume_available() else "#recruiter"
    resume_attrs = ' download="Anu_A_Resume.pdf"' if resume_available() else ""

    stats = [
        (str(len(projects)).zfill(2), "Featured builds"),
        (str(len(profile["experience"])).zfill(2), "Experience roles"),
        (str(len(profile["certifications"])).zfill(2), "Certifications"),
        (str(len(profile["education"])).zfill(2), "Degrees"),
    ]
    stat_html = "".join(
        f'<div class="stat"><strong>{value}</strong><span>{escape(label)}</span></div>'
        for value, label in stats
    )

    portrait = (
        f'<img src="{image_uri}" alt="Portrait of {name}">'
        if image_uri
        else f'<div class="portrait-placeholder">{escape(profile["initials"])}</div>'
    )

    st.markdown(
        f"""
        <div id="home" class="anchor"></div>
        <section class="hero">
          <div class="hero-copy">
            <div class="status"><span class="status-dot"></span>{escape(profile["availability"])}</div>
            <div class="eyebrow">{escape(profile["role_line"])} · {escape(profile["location"])}</div>
            <h1>
              <span class="line">Hi, I'm {name}.</span>
              <span class="line">I build <span class="grad">intelligent</span></span>
              <span class="line">products.</span>
            </h1>
            <p class="lead">{escape(profile["intro"])}</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#projects">Explore projects ↘</a>
              <a class="btn btn-ghost" href="{escape(profile["links"]["github"])}" target="_blank" rel="noopener">GitHub profile ↗</a>
              <a class="btn btn-ghost" href="{resume_href}"{resume_attrs}>Download resume ↓</a>
            </div>
            <div class="stat-row">{stat_html}</div>
          </div>
          <div class="hero-visual">
            <div class="portrait-frame">{portrait}</div>
            <div class="float-chip one"><span class="dot"></span>Python · GenAI</div>
            <div class="float-chip two"><span class="dot violet"></span>ML · Data</div>
          </div>
        </section>
        <div class="marquee" aria-hidden="true">
          <div class="marquee-track">{_marquee_group()}{_marquee_group()}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
