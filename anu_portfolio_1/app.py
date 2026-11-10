import streamlit as st

from components.about import render_about
from components.certifications import render_certifications
from components.contact import render_contact
from components.education import render_education
from components.experience import render_experience
from components.faq import render_faq
from components.footer import render_footer
from components.github_activity import render_github_activity
from components.hero import render_hero
from components.leadership import render_leadership
from components.navigation import render_navigation
from components.projects import render_projects
from components.recruiter import render_recruiter
from components.skills import render_skills
from components.theme import inject_styles
from utils.github import fetch_github_repos

st.set_page_config(
    page_title="Anu A | AI & Python Developer",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

raw_theme = st.query_params.get("theme", "dark")
if isinstance(raw_theme, (list, tuple)):
    raw_theme = raw_theme[0] if raw_theme else "dark"
theme = "light" if str(raw_theme).lower() == "light" else "dark"

inject_styles(theme)

render_navigation(theme)
render_hero()
render_about()
render_skills()

with st.spinner("Syncing public repositories..."):
    snapshot = fetch_github_repos()

render_projects(snapshot)
render_experience()
render_education()
render_certifications()
render_leadership()
render_github_activity(snapshot)
render_recruiter()
render_faq()
render_contact()
render_footer()
