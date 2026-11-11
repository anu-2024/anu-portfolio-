"""
Anu A - 3D Portfolio (Streamlit)

You normally never need to edit this file.
 - Content & colours  -> portfolio_data.py
 - Look & 3D scene    -> template/portfolio.html
Run locally:  streamlit run app.py
"""
import base64
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

import portfolio_data as cfg

BASE = Path(__file__).parent

st.set_page_config(
    page_title=cfg.PAGE_TITLE,
    page_icon=cfg.PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)


def read_b64(rel_path: str) -> str:
    """Return a file as base64, or '' if it does not exist."""
    p = BASE / rel_path
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else ""


def build_page() -> str:
    photo = read_b64(cfg.PHOTO_FILE)
    data = {
        "theme": cfg.THEME,
        "profile": cfg.PROFILE,
        "stats": cfg.STATS,
        "links": [l for l in cfg.LINKS if l[1]],
        "skillGroups": cfg.SKILL_GROUPS,
        "experience": cfg.EXPERIENCE,
        "projects": cfg.PROJECTS,
        "education": cfg.EDUCATION,
        "certifications": cfg.CERTIFICATIONS,
        "achievements": cfg.ACHIEVEMENTS,
        "photo": f"data:image/jpeg;base64,{photo}" if photo else "",
        "resumeB64": read_b64(cfg.RESUME_FILE),
        "resumeName": cfg.RESUME_DOWNLOAD_NAME,
        "title": cfg.PAGE_TITLE,
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (BASE / "template" / "portfolio.html").read_text(encoding="utf-8")
    return html.replace("/*__DATA__*/null", payload)


# Make the portfolio fill the whole browser window and hide Streamlit's own chrome.
st.markdown(
    f"""
    <style>
      header[data-testid="stHeader"], footer, #MainMenu,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] {{ display:none !important; }}
      html, body, .stApp, [data-testid="stAppViewContainer"] {{
        background:{cfg.THEME["bg"]} !important; overflow:hidden !important; }}
      .block-container, [data-testid="stMainBlockContainer"] {{
        padding:0 !important; max-width:100% !important; }}
      iframe {{ position:fixed; inset:0; width:100vw; height:100vh;
                border:0; z-index:999; }}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_page(), height=900, scrolling=True)
