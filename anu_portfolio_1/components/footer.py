import streamlit as st

from utils.data import load_profile
from utils.text import escape


def render_footer() -> None:
    profile = load_profile()
    links = profile["links"]
    st.markdown(
        f"""
        <footer class="footer">
          <span>Designed and built with intention · {escape(profile["name"])} · {escape(profile["location"])}</span>
          <span>
            <a href="#home">Back to top ↑</a>
            &nbsp;·&nbsp;
            <a href="{escape(links["github"])}" target="_blank" rel="noopener">GitHub</a>
            &nbsp;·&nbsp;
            <a href="{escape(links["linkedin"])}" target="_blank" rel="noopener">LinkedIn</a>
          </span>
        </footer>
        """,
        unsafe_allow_html=True,
    )
