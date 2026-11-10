import streamlit as st

from components.ui import section_header
from utils.assets import resume_available, resume_data_uri
from utils.data import load_profile
from utils.text import escape


def render_contact() -> None:
    profile = load_profile()
    links = profile["links"]
    resume_href = resume_data_uri() if resume_available() else "#recruiter"
    resume_attrs = ' download="Anu_A_Resume.pdf"' if resume_available() else ""
    phone_href = "tel:" + profile["phone"].replace(" ", "")

    section_header(
        "contact",
        "11",
        "Contact",
        "Let's build something useful.",
        "Open to internships, entry-level roles and conversations about AI, Python and data.",
    )

    st.markdown(
        f"""
        <div class="panel contact-card">
          <span class="eyebrow">Open to opportunities</span>
          <h2>Have a role, a project or a question?</h2>
          <p>{escape(profile["summary"])} I am based in {escape(profile["location"])} and open to remote opportunities.</p>
          <div class="contact-links">
            <a class="btn btn-primary" href="mailto:{escape(profile["email"])}">Email Anu ↗</a>
            <a class="btn btn-ghost" href="{escape(links["linkedin"])}" target="_blank" rel="noopener">Connect on LinkedIn ↗</a>
            <a class="btn btn-ghost" href="{resume_href}"{resume_attrs}>Download resume ↓</a>
          </div>
          <div class="contact-grid">
            <div class="contact-item"><span>Email</span><a href="mailto:{escape(profile["email"])}">{escape(profile["email"])}</a></div>
            <div class="contact-item"><span>Phone</span><a href="{escape(phone_href)}">{escape(profile["phone"])}</a></div>
            <div class="contact-item"><span>Location</span><strong>{escape(profile["location"])}</strong></div>
            <div class="contact-item"><span>GitHub</span><a href="{escape(links["github"])}" target="_blank" rel="noopener">github.com/anu-2024</a></div>
            <div class="contact-item"><span>LinkedIn</span><a href="{escape(links["linkedin"])}" target="_blank" rel="noopener">linkedin.com/in/anu-a-</a></div>
            <div class="contact-item"><span>HackerRank</span><a href="{escape(links["hackerrank"])}" target="_blank" rel="noopener">Coding profile ↗</a></div>
            <div class="contact-item"><span>LeetCode</span><a href="{escape(links["leetcode"])}" target="_blank" rel="noopener">Problem solving ↗</a></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
