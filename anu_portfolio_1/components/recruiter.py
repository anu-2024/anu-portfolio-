import streamlit as st

from components.ui import chip_list, section_header
from utils.assets import resume_available, resume_bytes, resume_data_uri
from utils.data import load_profile
from utils.text import escape


def render_recruiter() -> None:
    profile = load_profile()
    education = profile["education"][0]
    roles = chip_list(profile["roles_of_interest"])
    resume_href = resume_data_uri() if resume_available() else "#contact"
    resume_attrs = ' download="Anu_A_Resume.pdf"' if resume_available() else ""

    section_header(
        "recruiter",
        "09",
        "Recruiter quick view",
        "The short version, for busy people.",
        "A concise summary of the profile, the roles of interest and the fastest ways to get in touch.",
    )

    st.markdown(
        f"""
        <div class="panel recruiter-card">
          <div class="recruiter-grid">
            <div>
              <span class="eyebrow">At a glance</span>
              <h2>AI applications, Python and data.</h2>
              <p>{escape(profile["summary"])}</p>
              <div class="recruiter-facts">
                <div class="fact-row"><span>Location</span><strong>{escape(profile["location"])}</strong></div>
                <div class="fact-row"><span>Education</span><strong>{escape(education["degree"])} · {escape(education["institution"])} · {escape(education["period"])}</strong></div>
                <div class="fact-row"><span>Experience</span><strong>1M1B · CCSI Computer Education · Academor</strong></div>
                <div class="fact-row"><span>Availability</span><strong>{escape(profile["availability"])}</strong></div>
              </div>
            </div>
            <div>
              <span class="eyebrow">Roles of interest</span>
              <div class="role-list">{roles}</div>
              <div class="rule" style="border-top:1px solid var(--line);margin:1.2rem 0;"></div>
              <span class="eyebrow">What I bring</span>
              <ul class="detail-list" style="margin-top:0.6rem;">
                <li>Hands-on experience building AI-enabled, machine-learning and data-driven applications.</li>
                <li>Practical Python development across Streamlit, Flask, Django and API workflows.</li>
                <li>Clear technical communication, supported by programming instruction experience.</li>
                <li>A learning mindset and a focus on solving real user problems.</li>
              </ul>
              <div class="contact-links">
                <a class="btn btn-primary" href="mailto:{escape(profile["email"])}">Email Anu ↗</a>
                <a class="btn btn-ghost" href="{resume_href}"{resume_attrs}>Download resume ↓</a>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if resume_available():
        st.download_button(
            "Download resume (PDF)",
            data=resume_bytes(),
            file_name="Anu_A_Resume.pdf",
            mime="application/pdf",
            key="recruiter_resume",
        )
    else:
        st.caption("Resume file is not available in this deployment.")
