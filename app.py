import os
from datetime import datetime, timezone
from urllib.parse import quote

import requests
import streamlit as st

st.set_page_config(
    page_title="Anu A | AI & Python Developer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GITHUB_USER = "anu-2024"
GITHUB_API = f"https://api.github.com/users/{GITHUB_USER}/repos"
GITHUB_PROFILE = f"https://github.com/{GITHUB_USER}"
LINKEDIN = "https://www.linkedin.com/in/anu-a-/"
EMAIL = "anuanjenappa@gmail.com"
PHONE = "+91 7259109591"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --bg:#080b14; --panel:#101626; --panel2:#131d30; --text:#edf2ff; --muted:#9ba8bd; --line:rgba(166,185,220,.14); --violet:#9b8cff; --cyan:#65d8e8; }
html, body, [class*="css"] { font-family:'Manrope',sans-serif; }
.stApp { background:radial-gradient(ellipse at 82% 0%, rgba(107,82,220,.18), transparent 34%), radial-gradient(ellipse at 4% 25%, rgba(41,178,196,.10), transparent 28%), var(--bg); color:var(--text); }
.block-container { max-width:1180px; padding-top:1.2rem; padding-bottom:4rem; }
header, footer {visibility:hidden;}
h1,h2,h3 { color:var(--text)!important; letter-spacing:-.04em; }
p, li { color:#c2cce0; }
a { color:var(--cyan)!important; text-decoration:none!important; }
a:hover { color:var(--violet)!important; }
.eyebrow { color:var(--cyan); font:500 11px 'DM Mono',monospace; letter-spacing:.18em; text-transform:uppercase; }
.hero { padding:3.1rem 0 2.4rem; }
.hero-title { font-size:clamp(2.7rem,6vw,5.1rem); line-height:1.02; font-weight:800; letter-spacing:-.07em; margin:.6rem 0 1rem; color:#f5f7ff; }
.gradient { background:linear-gradient(100deg,#a99cff 10%,#6bd9e8 90%); -webkit-background-clip:text; background-clip:text; color:transparent; }
.lead { color:#b9c5d9; font-size:1.08rem; line-height:1.85; max-width:720px; }
.pill { display:inline-block; border:1px solid rgba(155,140,255,.32); color:#d8d2ff; background:rgba(155,140,255,.09); border-radius:30px; padding:7px 12px; margin:4px 5px 4px 0; font:11px 'DM Mono',monospace; }
.panel { background:linear-gradient(145deg,rgba(21,31,51,.96),rgba(13,19,32,.96)); border:1px solid var(--line); border-radius:18px; padding:22px; height:100%; box-shadow:0 14px 40px rgba(0,0,0,.12); }
.project { background:linear-gradient(145deg,rgba(21,31,51,.98),rgba(12,18,31,.98)); border:1px solid var(--line); border-radius:18px; padding:22px; min-height:255px; transition:transform .2s,border-color .2s; }
.project:hover { transform:translateY(-4px); border-color:rgba(101,216,232,.48); }
.project-kicker { color:var(--cyan); font:11px 'DM Mono',monospace; letter-spacing:.12em; text-transform:uppercase; }
.project h3 { margin:.5rem 0; font-size:1.18rem; }
.muted { color:var(--muted); font-size:.91rem; line-height:1.7; }
.metric { font-size:1.8rem; font-weight:800; color:#f3f5ff; }
.section-label { margin:3.2rem 0 1.2rem; }
.section-label h2 { font-size:2rem; margin:.25rem 0; }
.rule { border-top:1px solid var(--line); margin:1.2rem 0; }
.skill { border:1px solid var(--line); border-radius:12px; padding:13px 15px; background:rgba(17,26,43,.7); margin-bottom:10px; }
.timeline { border-left:1px solid rgba(155,140,255,.45); padding-left:20px; margin:8px 0 22px; }
.timeline-item { position:relative; margin:0 0 22px; }
.timeline-item:before { content:''; position:absolute; left:-25px; top:7px; width:9px; height:9px; border-radius:50%; background:var(--cyan); box-shadow:0 0 0 4px rgba(101,216,232,.12); }
.stButton>button, .stDownloadButton>button { border-radius:999px; border:1px solid rgba(155,140,255,.5); background:linear-gradient(100deg,rgba(155,140,255,.18),rgba(101,216,232,.12)); color:#f2f4ff; padding:.55rem 1.1rem; font-weight:700; }
.stButton>button:hover, .stDownloadButton>button:hover { border-color:var(--cyan); color:white; }
div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { background:#101827; color:#edf2ff; border:1px solid var(--line); border-radius:12px; }
div[data-testid="stAlert"] { background:#111b2d; }
img { border-radius:18px; }
.small-note { color:#8291aa; font-size:.78rem; }
</style>
""", unsafe_allow_html=True)

def section(kicker, title, subtitle=None):
    st.markdown(f'<div class="section-label"><div class="eyebrow">{kicker}</div><h2>{title}</h2>{f"<div class=muted>{subtitle}</div>" if subtitle else ""}</div>', unsafe_allow_html=True)

def safe_text(value, fallback=""):
    return value if isinstance(value, str) else fallback

@st.cache_data(ttl=600, show_spinner=False)
def get_github_repos():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Anu-Portfolio"}
    token = st.secrets.get("GITHUB_TOKEN", "") if hasattr(st, "secrets") else ""
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(GITHUB_API, params={"sort":"updated","per_page":100,"type":"owner"}, headers=headers, timeout=12)
    response.raise_for_status()
    return response.json()

def get_repo_data():
    try:
        repos = get_github_repos()
        repos = [r for r in repos if not r.get("fork") and not r.get("private")]
        repos.sort(key=lambda r: r.get("updated_at") or "", reverse=True)
        return repos, None
    except Exception as exc:
        return [], str(exc)

def project_card(kicker, title, description, stack, repo_url, demo_url=None):
    st.markdown(f"""
    <div class="project">
      <div class="project-kicker">{kicker}</div>
      <h3>{title}</h3>
      <div class="muted">{description}</div>
      <div style="margin-top:13px;color:#b9c7df;font:11px 'DM Mono',monospace;">{stack}</div>
      <div style="margin-top:17px;"><a href="{repo_url}" target="_blank">↗ Source code</a>{f' &nbsp;·&nbsp; <a href="{demo_url}" target="_blank">Live demo</a>' if demo_url else ''}</div>
    </div>""", unsafe_allow_html=True)

# Top navigation
nav = st.columns([2.2,1,1,1,1,1])
with nav[0]:
    st.markdown('<div style="font-weight:800;font-size:1.15rem;letter-spacing:-.04em;">anu<span class="gradient">.dev</span> <span class="small-note">/ portfolio</span></div>', unsafe_allow_html=True)
for col, label, anchor in zip(nav[1:], ["About","Projects","Experience","Skills","Contact"], ["about","projects","experience","skills","contact"]):
    with col:
        st.markdown(f'<div style="text-align:right;padding-top:6px;"><a href="#{anchor}" style="color:#aebbd0!important;font-size:.83rem;">{label}</a></div>', unsafe_allow_html=True)

# Hero
st.markdown('<div class="hero"><div class="eyebrow">MCA · AI & GENERATIVE AI · BENGALURU, INDIA</div><div class="hero-title">Building useful things<br>with <span class="gradient">intelligent technology.</span></div><div class="lead">I’m Anu A — an emerging AI and Python developer focused on turning ideas into practical applications. I work across Generative AI, machine learning, data-driven products and application development.</div><div style="margin-top:20px;"><span class="pill">Python</span><span class="pill">Generative AI</span><span class="pill">Machine Learning</span><span class="pill">Streamlit</span><span class="pill">APIs</span><span class="pill">SQL</span></div></div>', unsafe_allow_html=True)
left, right = st.columns([1.65,1], gap="large")
with left:
    c1,c2,c3 = st.columns(3)
    for col, number, label in [(c1,"06+","Selected projects"),(c2,"03","Internship / work roles"),(c3,"08+","Certifications")]:
        with col:
            st.markdown(f'<div class="panel"><div class="metric">{number}</div><div class="muted">{label}</div></div>', unsafe_allow_html=True)
    st.write("")
    a,b = st.columns([1,1])
    with a:
        st.link_button("Explore projects ↘", "#projects", use_container_width=True)
    with b:
        st.link_button("GitHub profile ↗", GITHUB_PROFILE, use_container_width=True)
with right:
    st.image("assets/anu-profile.png", use_container_width=True)
    st.markdown('<div class="small-note" style="text-align:center;">AI & Generative AI Developer · Python · ML</div>', unsafe_allow_html=True)

# About
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
section("01 / THE PERSON BEHIND THE BUILDS", "Curious by nature. Practical by design.")
a,b = st.columns([1.3,1], gap="large")
with a:
    st.markdown("""
    <div class="panel">
    <p>I’m currently pursuing a <b>Master of Computer Applications at Alliance University</b>. My interests sit at the intersection of AI, software engineering and data — especially applications that make complex tasks simpler for people.</p>
    <p>My experience includes building Python and machine-learning applications, experimenting with Generative AI and agent workflows, and helping learners develop programming fundamentals as an IT Trainer.</p>
    <p>I value clear problem-solving, continuous learning and building technology that can be demonstrated, tested and improved.</p>
    </div>""", unsafe_allow_html=True)
with b:
    st.markdown("""
    <div class="panel">
      <div class="eyebrow">CURRENT FOCUS</div>
      <h3>From prototype to useful product</h3>
      <div class="rule"></div>
      <div class="muted">01 · LLM applications & AI agents</div>
      <div class="muted">02 · Python APIs and application development</div>
      <div class="muted">03 · Machine learning and data workflows</div>
      <div class="muted">04 · Responsible, user-centred product thinking</div>
      <div class="rule"></div>
      <div class="eyebrow">EDUCATION</div>
      <b>MCA · Alliance University</b><div class="muted">2025–2027 · Bengaluru</div>
      <br><b>BCA · St. Francis de Sales College</b><div class="muted">2021–2024 · Bengaluru</div>
    </div>""", unsafe_allow_html=True)

# Projects
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
section("02 / SELECTED WORK", "Projects with a purpose", "A curated selection of practical builds. Open the source code to explore implementation details.")
projects = [
    ("AI AGENT · FEATURED","CymbalMart Shopping Agent","An AI shopping assistant that translates natural-language event needs into personalised, budget-conscious product suggestions and curated carts.","Gemini · Google AI Studio · React · TypeScript","https://github.com/anu-2024/CymbalMart-Shopping-Agent"),
    ("SUSTAINABILITY · FEATURED","Green Route Travel Recommendation System","A route recommendation experience with 1,500+ India travel routes, ML model comparison and Dijkstra-based route optimisation.","Python · ML · Streamlit · Pandas · Plotly","https://github.com/anu-2024/GR-TRAVEL-RECOMMENDATION-","https://exd5h3xk8bbeayvwrzyogl.streamlit.app/"),
    ("COMMUNITY TECH","Community Resource Sharing System","A platform connecting people who want to donate or request unused household items, with a Spring Boot backend and Streamlit interface.","Java · Spring Boot · Streamlit · SQLite","https://github.com/anu-2024/Community-Resource-Sharing-System","https://community-resource-sharing-system-fmd9b93drahlbslzwxeap7.streamlit.app/"),
    ("MACHINE LEARNING","AQI Prediction System","A Flask application that predicts AQI from pollutant measurements, supported by data preprocessing, EDA, model training and evaluation.","Python · Random Forest · Flask · Scikit-learn","https://github.com/anu-2024/AQI_Capstone_Project"),
    ("AI · OPENENV","Smart Waste Management OpenEnv","A simulated municipal complaint-resolution environment where an AI agent classifies waste complaints, assigns departments, dispatches trucks and completes cleanup through a staged API workflow.","Python · FastAPI · OpenEnv · Hugging Face · Docker","https://github.com/anu-2024/smart-waste-openenv","https://qwerty123g45-smart-waste-openenv.hf.space/docs"),
    ("COMPUTER VISION · OCR","Visual Search + OCR Comparison","A browser-based visual search application comparing Tesseract.js and TrOCR, with object detection, text extraction and OCR evaluation tools.","Next.js · TypeScript · TensorFlow.js · Tesseract.js · TrOCR","https://github.com/anu-2024/VISUAL-SEARCH-WITH-OCR-COMPARISON-"),
    ("NLP · REINFORCEMENT LEARNING","Emergency Message Prioritization System","A human-in-the-loop decision-support prototype that combines classical NLP with a reinforcement-learning queue simulator and a transparent rule-based baseline. It never dispatches emergency services autonomously.","Python · Streamlit · TF-IDF · Logistic Regression · DQN","https://github.com/anu-2024/Emergency-Message-Prioritization-System"),
]
for row in [projects[i:i+2] for i in range(0,len(projects),2)]:
    cols = st.columns(2, gap="medium")
    for col, item in zip(cols,row):
        with col:
            project_card(*item)

st.markdown('<div class="small-note">Project summaries are based on the supplied technical profiles. Replace each general GitHub profile link with its exact repository URL after confirming the matching repository.</div>', unsafe_allow_html=True)

# GitHub live area
section("03 / LIVE FROM GITHUB", "The work keeps moving", "Public repositories are fetched directly from GitHub. New public repositories and metadata changes appear here on the next refresh.")
repos, repo_error = get_repo_data()
if repos:
    st.caption(f"Showing {min(len(repos),12)} of {len(repos)} public, non-fork repositories · Data refreshes every 10 minutes when the page reruns.")
    cols = st.columns(3)
    for idx, repo in enumerate(repos[:12]):
        with cols[idx%3]:
            lang = repo.get("language") or "Multiple / not specified"
            desc = safe_text(repo.get("description"), "No repository description yet.")
            updated = (repo.get("updated_at") or "")[:10]
            st.markdown(f"""
            <div class="project" style="min-height:190px;margin-bottom:14px;">
              <div class="project-kicker">{lang}</div>
              <h3>{repo.get('name','Repository')}</h3>
              <div class="muted">{desc[:150]}</div>
              <div style="margin-top:12px;color:#9ba8bd;font:11px 'DM Mono',monospace;">★ {repo.get('stargazers_count',0)} &nbsp;⑂ {repo.get('forks_count',0)} &nbsp; Updated {updated}</div>
              <div style="margin-top:12px;"><a href="{repo.get('html_url',GITHUB_PROFILE)}" target="_blank">↗ View repository</a></div>
            </div>""", unsafe_allow_html=True)
    if st.button("Refresh GitHub data", key="refresh_github"):
        get_github_repos.clear()
        st.rerun()
else:
    st.markdown(f'<div class="panel"><b>Live repository feed is temporarily unavailable.</b><div class="muted">The curated project showcase remains available. Check your network or GitHub API rate limit and refresh later.</div><a href="{GITHUB_PROFILE}" target="_blank">Open GitHub profile ↗</a></div>', unsafe_allow_html=True)
    if repo_error:
        st.caption("Connection detail: " + repo_error[:180])

# Experience
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
section("04 / EXPERIENCE", "Learning by building and teaching")
c1,c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    <div class="panel">
    <div class="timeline">
      <div class="timeline-item"><div class="eyebrow">FEB 2026 – MAR 2026 · REMOTE</div><h3>1M1B Green Internship</h3><div class="muted">Worked on distance-based emission calculations, data processing and interactive visualisations using Pandas, Streamlit and Plotly to support more sustainable travel decisions.</div></div>
      <div class="timeline-item"><div class="eyebrow">APR 2025 – NOV 2025 · BENGALURU</div><h3>IT Trainer · CCSI Computer Education</h3><div class="muted">Conducted practical programming sessions in Python, Java, C and C++, guiding learners through coding concepts and project work.</div></div>
      <div class="timeline-item"><div class="eyebrow">FEB 2024 – MAR 2024 · REMOTE</div><h3>Data Science Intern · Academor</h3><div class="muted">Applied Python, Pandas, NumPy, Scikit-learn and Matplotlib to data preprocessing, exploratory analysis, model development and visualisation.</div></div>
    </div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="panel">
      <div class="eyebrow">LEADERSHIP</div><h3>Secretary · Rotaract Club</h3>
      <div class="muted">Served for one year, managing official correspondence and records while supporting communication across a 50+ member campus organisation.</div>
      <div class="rule"></div>
      <div class="eyebrow">CERTIFICATIONS & LEARNING</div>
      <ul>
        <li>Engineer AI Agents with Agent Development Kit — Google</li>
        <li>Data Analysis with Python — IBM</li>
        <li>Introduction to Databases — Meta</li>
        <li>Introduction to Front-End Development — Meta</li>
        <li>UI Design and Prototyping — Microsoft</li>
        <li>Applied Statistics for Data Analytics — DeepLearning.AI</li>
        <li>Advanced Data Structures and Algorithms — Packt</li>
        <li>Java Programming for Beginners — IBM</li>
      </ul>
    </div>""", unsafe_allow_html=True)

# Skills
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
section("05 / TOOLKIT", "Skills backed by hands-on work")
skill_groups = [
    ("Programming","Python · Java · C · C++ · JavaScript"),
    ("AI & Generative AI","Gemini · Google AI Studio · Agent Development Kit · Prompt Engineering · Hugging Face"),
    ("Machine Learning & Data","Pandas · NumPy · Scikit-learn · Matplotlib · Plotly"),
    ("Web & APIs","Django · Flask · FastAPI · HTML · CSS · React basics"),
    ("Databases & Tools","MySQL · SQLite · MongoDB · GitHub · VS Code · Streamlit · Docker"),
]
cols=st.columns(2)
for i,(name,items) in enumerate(skill_groups):
    with cols[i%2]:
        st.markdown(f'<div class="skill"><div class="eyebrow">{name}</div><div style="margin-top:7px;color:#d7e0f2;">{items}</div></div>',unsafe_allow_html=True)

# Recruiter quick view
section("06 / FOR RECRUITERS", "A quick introduction")
st.markdown("""
<div class="panel">
<b>What I bring</b>
<ul>
<li>Hands-on experience building AI-enabled, machine-learning and data-driven applications.</li>
<li>Practical Python development experience across Streamlit, Flask, Django and API workflows.</li>
<li>Ability to communicate technical concepts, supported by programming instruction experience.</li>
<li>A learning mindset, collaborative approach and interest in solving real user problems.</li>
</ul>
<b>Roles of interest:</b> Generative AI / AI Application Intern · Python Developer · Machine Learning Intern · Data / Software Engineering Intern.
</div>""", unsafe_allow_html=True)
resume_path = "assets/anu-resume.pdf"
with open(resume_path,"rb") as f:
    st.download_button("Download resume ↓", data=f.read(), file_name="Anu_A_Resume.pdf", mime="application/pdf")

# Local profile assistant
section("07 / ASK ABOUT MY WORK", "Meet the portfolio assistant", "A lightweight profile assistant using verified information on this page.")
question = st.text_input("Ask a question", placeholder="e.g. Which projects use Generative AI?")
if question:
    q = question.lower()
    if any(k in q for k in ["genai","generative","agent","gemini","llm"]):
        answer = "My Generative AI work includes the CymbalMart Shopping Agent, built with Gemini and Google AI Studio, and my learning around Google's Agent Development Kit. The project focuses on natural-language shopping requirements and personalised recommendations."
    elif any(k in q for k in ["python","machine learning","ml","data"]):
        answer = "My Python and ML work includes Green Route, AQI Prediction and AgriNEWS. My toolkit includes Python, Pandas, NumPy, Scikit-learn, Streamlit, Flask and Django."
    elif any(k in q for k in ["experience","intern","work","trainer"]):
        answer = "I completed the 1M1B Green Internship, worked as an IT Trainer at CCSI Computer Education, and completed a Data Science internship at Academor."
    elif any(k in q for k in ["education","degree","college","mca"]):
        answer = "I am pursuing an MCA at Alliance University (2025–2027), after completing a BCA at St. Francis de Sales College (2021–2024)."
    elif any(k in q for k in ["contact","email","linkedin","hire","resume"]):
        answer = f"You can contact me at {EMAIL}, connect on LinkedIn ({LINKEDIN}), or download my resume above."
    elif any(k in q for k in ["skill","technology","stack","tools"]):
        answer = "My skills include Python, Java, C/C++, JavaScript, Gemini, ADK, Pandas, NumPy, Scikit-learn, Django, Flask, FastAPI, Streamlit, SQL, MongoDB and Docker."
    else:
        answer = "I can help with questions about Anu's projects, skills, education, experience and contact details. Try asking about Generative AI projects, Python skills or internship experience."
    st.markdown(f'<div class="panel">{answer}</div>', unsafe_allow_html=True)

# Contact
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
section("08 / LET'S CONNECT", "Have a problem worth solving?")
st.markdown(f"""
<div class="panel">
<div class="lead" style="font-size:1rem;">I’m open to opportunities where I can contribute, learn quickly and build meaningful technology with a team.</div>
<div class="rule"></div>
<div><b>Email</b> · <a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><b>LinkedIn</b> · <a href="{LINKEDIN}" target="_blank">Connect with me ↗</a></div>
<div><b>GitHub</b> · <a href="{GITHUB_PROFILE}" target="_blank">Explore my repositories ↗</a></div>
<div><b>HackerRank</b> · <a href="https://www.hackerrank.com/profile/anuanjenappa" target="_blank">Coding profile ↗</a></div>
<div><b>LeetCode</b> · <a href="https://leetcode.com/u/Anu_A_2" target="_blank">Problem solving ↗</a></div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;padding:35px 0 5px;color:#75839b;font-size:.8rem;">Designed & built with intention · Anu A · Bengaluru, India</div>', unsafe_allow_html=True)
