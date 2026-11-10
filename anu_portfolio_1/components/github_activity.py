import streamlit as st

from components.ui import section_header
from utils.github import (
    GITHUB_PROFILE,
    GitHubSnapshot,
    clear_github_cache,
    language_mix,
    other_repos,
    repo_stats,
)
from utils.text import escape, format_date, format_datetime, format_number, truncate


def _repo_card(repo: dict) -> str:
    name = escape(repo.get("name") or "Repository")
    url = escape(repo.get("html_url") or GITHUB_PROFILE)
    language = escape(repo.get("language") or "Not specified")
    description = escape(truncate(repo.get("description") or "No description provided.", 170))
    stars = format_number(repo.get("stargazers_count"))
    forks = format_number(repo.get("forks_count"))
    updated = format_date(repo.get("updated_at"))
    return f"""
      <div class="panel repo-card">
        <div class="project-kicker">{language}</div>
        <h3><a href="{url}" target="_blank" rel="noopener">{name}</a></h3>
        <p>{description}</p>
        <div class="repo-meta">
          <span>★ {stars}</span>
          <span>⑂ {forks}</span>
          <span>Updated {updated}</span>
        </div>
        <a class="repo-link" href="{url}" target="_blank" rel="noopener">Open repository ↗</a>
      </div>
    """


def render_github_activity(snapshot: GitHubSnapshot) -> None:
    section_header(
        "github",
        "08",
        "GitHub activity",
        "The work keeps moving.",
        "Public repository data fetched directly from the GitHub REST API, with featured work separated from other public repositories.",
    )

    if st.session_state.pop("github_refreshed", False):
        st.toast("GitHub data refreshed.")

    last_sync = format_datetime(snapshot.fetched_at)
    note = (
        f'<div class="github-note">Last synced: <strong style="color:var(--text);">{escape(last_sync)}</strong> · '
        f'Cached for 10 minutes · <a href="{GITHUB_PROFILE}" target="_blank" rel="noopener">Open GitHub profile ↗</a></div>'
    )

    left, right = st.columns([3.4, 1.2], vertical_alignment="center")
    with left:
        st.markdown(note, unsafe_allow_html=True)
    with right:
        refresh = st.button("Refresh GitHub data", key="refresh_github", use_container_width=True)

    if refresh:
        clear_github_cache()
        st.session_state["github_refreshed"] = True
        st.rerun()

    if snapshot.error:
        st.markdown(
            f"""
            <div class="error-panel">
              <span class="glyph">◌</span>
              <div>
                <strong>Live repository data is temporarily unavailable.</strong>
                <p>{escape(snapshot.error)} The curated project showcase above remains available.</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    repos = snapshot.repos
    stats = repo_stats(repos)
    languages = language_mix(repos)
    others = other_repos(repos)

    st.markdown(
        f"""
        <div class="metric-row">
          <div class="panel metric-card"><strong>{format_number(stats["repositories"])}</strong><span>Public repositories</span></div>
          <div class="panel metric-card"><strong>{format_number(stats["stars"])}</strong><span>Total stars</span></div>
          <div class="panel metric-card"><strong>{format_number(stats["forks"])}</strong><span>Total forks</span></div>
          <div class="panel metric-card"><strong>{format_number(stats["languages"])}</strong><span>Languages used</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    language_rows = "".join(
        f"""
        <div class="language-line">
          <span class="name">{escape(item["language"])}</span>
          <div class="lang-track"><div class="lang-fill" style="width:{item["percent"]}%"></div></div>
          <span class="value">{item["percent"]:.0f}%</span>
        </div>
        """
        for item in languages
    )
    language_panel = (
        f"""
        <div class="panel">
          <span class="eyebrow">Language mix</span>
          <h3 style="margin:0.35rem 0 0.9rem;font-size:1.05rem;">Primary languages</h3>
          <div class="language-bars">{language_rows}</div>
          <p class="github-note" style="margin-top:0.9rem;">Based on the primary language reported for each public, non-fork repository.</p>
        </div>
        """
        if language_rows
        else """
        <div class="panel">
          <span class="eyebrow">Language mix</span>
          <h3 style="margin:0.35rem 0 0.5rem;font-size:1.05rem;">Language data unavailable</h3>
          <p class="github-note">GitHub did not return a primary language for the available repositories.</p>
        </div>
        """
    )

    other_cards = "".join(_repo_card(repo) for repo in others[:12])
    others_panel = (
        f'<div class="repo-grid">{other_cards}</div>'
        if other_cards
        else """
        <div class="panel">
          <span class="eyebrow">Other repositories</span>
          <h3 style="margin:0.35rem 0 0.5rem;font-size:1.05rem;">No additional public repositories</h3>
          <p class="github-note">GitHub did not return any other public, non-fork repositories beyond the featured project showcase.</p>
        </div>
        """
    )

    other_count = len(others)
    st.markdown(
        f"""
        <div class="github-grid">
          {language_panel}
          <div>
            <div class="github-toolbar" style="margin-bottom:0.7rem;">
              <span class="eyebrow">Other public repositories · {format_number(other_count)}</span>
              <span class="github-note">Featured repositories are curated above.</span>
            </div>
            {others_panel}
          </div>
        </div>
        <p class="github-note" style="margin-top:1rem;">Repository discovery is automatic. The seven featured repositories are curated in the project section; the rest appear here when GitHub returns them.</p>
        """,
        unsafe_allow_html=True,
    )
