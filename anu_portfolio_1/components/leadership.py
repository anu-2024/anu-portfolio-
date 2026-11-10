import streamlit as st

from components.ui import chip_list, section_header
from utils.data import load_profile
from utils.text import escape


def render_leadership() -> None:
    profile = load_profile()
    leadership = profile["leadership"]

    section_header(
        "leadership",
        "07",
        "Leadership",
        "Responsibility beyond the code.",
        "A student leadership role focused on records, correspondence and clear communication across a team.",
    )

    st.markdown(
        f"""
        <div class="leadership-grid">
          <div class="panel leadership-feature">
            <div class="leadership-mark">RC</div>
            <span class="eyebrow">Rotaract Club</span>
            <h2>{escape(leadership["role"])}</h2>
            <div class="leadership-org">{escape(leadership["organization"])}</div>
            <p>{escape(leadership["summary"])}</p>
            <div class="chips">{chip_list(["Records", "Correspondence", "Communication", "Responsibility"])}</div>
          </div>
          <div class="panel leadership-side">
            <span class="eyebrow">What it involved</span>
            <ul class="focus-list" style="margin-top:0.9rem;">
              <li><span class="num">01</span><span>Maintaining official records.</span></li>
              <li><span class="num">02</span><span>Managing official correspondence.</span></li>
              <li><span class="num">03</span><span>Supporting communication across the club.</span></li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
