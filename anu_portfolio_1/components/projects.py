import streamlit as st

from components.ui import chip_list, section_header
from utils.data import load_projects
from utils.github import GitHubSnapshot, find_repo, repo_language_breakdown
from utils.text import escape, format_date, format_number


def _repo_meta(repo: dict | None) -> str:
    if not repo:
        return ""
    parts = [
        f"★ {format_number(repo.get('stargazers_count'))}",
        f"⑂ {format_number(repo.get('forks_count'))}",
        f"Updated {format_date(repo.get('updated_at'))}",
    ]
    language = repo.get("language")
    if language:
        parts.insert(0, escape(language))
    return '<div class="project-meta">' + "".join(
        f"<span>{part}</span>" for part in parts
    ) + "</div>"


def _project_card(project: dict, snapshot: GitHubSnapshot) -> str:
    repo = find_repo(snapshot.repos, project["repo_name"])
    repo_url = escape(repo.get("html_url") if repo else project["repo"])
    demo = project.get("demo")
    demo_html = (
        f'<a class="card-link" href="{escape(demo)}" target="_blank" rel="noopener">'
        f'{escape(project["demo_label"])} ↗</a>'
        if demo
        else ""
    )
    return f"""
      <article class="project-card" style="--accent:{escape(project["accent"])};--accent-soft:{escape(project["accent_soft"])};">
        <div class="project-cover">
          <span class="cover-tag">{escape(project["cover_tag"])}</span>
          <span class="cover-index">{escape(project["index"])} / 07</span>
          <span class="cover-glyph">{escape(project["glyph"])}</span>
        </div>
        <div class="project-body">
          <div class="project-kicker">{escape(project["kicker"])}</div>
          <h3><a href="#detail-{escape(project["slug"])}">{escape(project["title"])}</a></h3>
          <p class="project-summary">{escape(project["summary"])}</p>
          <div class="chips">{chip_list(project["stack"])}</div>
          {_repo_meta(repo)}
          <div class="project-actions">
            <a class="card-link" href="#detail-{escape(project["slug"])}">Case study →</a>
            <a class="card-link" href="{repo_url}" target="_blank" rel="noopener">Code ↗</a>
            {demo_html}
          </div>
        </div>
      </article>
    """


def _language_rows(project: dict, snapshot: GitHubSnapshot) -> str:
    if not snapshot.repos:
        return ""
    breakdown = repo_language_breakdown(project["repo_name"])
    if not breakdown:
        return ""
    rows = "".join(
        f"""
        <div class="language-line">
          <span class="name">{escape(item["language"])}</span>
          <div class="lang-track"><div class="lang-fill" style="width:{item["percent"]}%"></div></div>
          <span class="value">{item["percent"]:.0f}%</span>
        </div>
        """
        for item in breakdown
    )
    return f"""
      <h4 style="margin-top:1.1rem;">Language mix</h4>
      <div class="language-bars">{rows}</div>
    """


def _project_detail(project: dict, snapshot: GitHubSnapshot) -> str:
    repo = find_repo(snapshot.repos, project["repo_name"])
    repo_url = escape(repo.get("html_url") if repo else project["repo"])
    demo = project.get("demo")
    demo_html = (
        f'<a class="btn btn-ghost" href="{escape(demo)}" target="_blank" rel="noopener">'
        f'{escape(project["demo_label"])} ↗</a>'
        if demo
        else ""
    )
    highlights = "".join(
        f"<li>{escape(item)}</li>" for item in project["highlights"]
    )
    return f"""
      <article class="project-detail" id="detail-{escape(project["slug"])}">
        <div class="detail-top">
          <a class="detail-back" href="#projects">← Back to all projects</a>
          <span class="detail-index">{escape(project["index"])} / 07</span>
        </div>
        <div class="detail-grid">
          <div class="panel detail-main">
            <span class="eyebrow">{escape(project["category"])} · Featured project</span>
            <h2>{escape(project["title"])}</h2>
            <p>{escape(project["summary"])}</p>
            <h3>Highlights</h3>
            <ul class="detail-list">{highlights}</ul>
            <h3>Stack</h3>
            <div class="chips">{chip_list(project["stack"])}</div>
          </div>
          <aside class="panel detail-side">
            <h4>Explore</h4>
            <div class="detail-links">
              <a class="card-link" href="{repo_url}" target="_blank" rel="noopener">View source on GitHub ↗</a>
              {demo_html}
              <a class="card-link muted" href="#projects">Back to project grid</a>
            </div>
            {_language_rows(project, snapshot)}
          </aside>
        </div>
      </article>
    """


def render_projects(snapshot: GitHubSnapshot) -> None:
    projects = load_projects()

    section_header(
        "projects",
        "03",
        "Featured projects",
        "Seven builds. Real problems. Measurable learning.",
        "A curated set of AI, machine-learning and full-stack projects. Open a card for the case study and source links.",
    )

    cards = "".join(_project_card(project, snapshot) for project in projects)
    st.markdown(f'<div class="project-grid">{cards}</div>', unsafe_allow_html=True)

    section_header(
        "case-studies",
        "03",
        "Project deep dives",
        "Inside the build.",
        "Select a project card to open its case study. Each view includes the problem, highlights, stack and links.",
        compact=True,
    )

    details = "".join(_project_detail(project, snapshot) for project in projects)
    st.markdown(
        f"""
        <div class="case-study-wrap">
          <div class="case-study-empty">
            <span class="arrow">↘</span>
            <span>Choose any featured project above to open its deep dive. Press “Back to all projects” to return to the grid.</span>
          </div>
          {details}
        </div>
        """,
        unsafe_allow_html=True,
    )
