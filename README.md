# Anu A — Developer Portfolio

A recruiter-focused portfolio for Anu A, built with Python and Streamlit. It combines a dark/light visual system, seven project case studies, live GitHub repository data, a local FAQ assistant and a downloadable resume.

The previous static HTML/CSS/JavaScript portfolio remains in `docs/` for GitHub Pages. The root `app.py` is now the Streamlit application.

## Features

- Responsive single-page portfolio with custom navigation
- Dark and light themes via `?theme=light` and `?theme=dark`
- Seven featured project cards with CSS-only case-study views
- Project technology stacks linked back to featured work
- Live GitHub data: public repositories, stars, forks, languages and update dates
- 10-minute GitHub cache with a manual refresh control
- Optional `GITHUB_TOKEN` secret for a higher GitHub API rate limit
- Recruiter Quick View with email, role interests and resume download
- Dedicated leadership section for the Rotaract Club Secretary role
- Rule-based local FAQ assistant with suggested questions
- Contact section with email, phone, LinkedIn, GitHub, HackerRank and LeetCode

## Project structure

```text
app.py                    Streamlit entry point
components/               Page sections and shared UI
  theme.py                CSS variables, layout and responsive styles
  navigation.py           Top navigation and theme toggle
  hero.py                 Hero section and resume link
  about.py                About and current focus
  skills.py               Technical skill groups
  projects.py             Project grid and case-study views
  experience.py           Experience timeline
  education.py            Education cards
  certifications.py       Certification grid
  leadership.py           Rotaract Club leadership profile
  github_activity.py      GitHub metrics, language mix and repositories
  recruiter.py            Recruiter Quick View
  faq.py                  Local FAQ assistant
  contact.py              Contact section
  footer.py               Footer
data/                     Verified content as JSON
utils/                    Data, asset, text and GitHub helpers
assets/                   Optimised portrait, favicon and resume PDF
.streamlit/               Streamlit configuration and optional secrets example
docs/                     Static GitHub Pages portfolio (preserved)
```

## Run locally

Requirements: Python 3.12+.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Tests

Run the local content, FAQ and asset checks:

```powershell
python -m unittest discover -s tests -v
```

For a Streamlit smoke test, run the app and confirm it loads without exceptions. The GitHub section handles API rate limits and network failures without blocking the rest of the portfolio.

## Optional GitHub token

The app works without a token. To raise the GitHub REST API rate limit, copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add a token with public repository read access:

```toml
GITHUB_TOKEN = "your_token_here"
```

Do not commit `.streamlit/secrets.toml`.

## Deploy to Streamlit Community Cloud

1. Push the project root to a GitHub repository.
2. In Streamlit Community Cloud, create an app from that repository.
3. Set the main file path to `app.py`.
4. Optionally add `GITHUB_TOKEN` under the app's secrets settings.
5. Deploy.

The app does not require a build step. `requirements.txt` installs Streamlit, Requests and Pandas.

## Content updates

- Profile, experience, education, certifications and leadership: `data/profile.json`
- Featured projects and repository names: `data/projects.json`
- Skill groups: `data/skills.json`
- FAQ answers and keywords: `data/faq.json`
- Portrait: `assets/anu-profile.jpg` and `assets/anu-profile-520.jpg`
- Resume: `assets/anu-resume.pdf`
- Visual system and responsive rules: `components/theme.py`

Only add achievements, metrics or dates that can be verified. The portfolio intentionally avoids unsupported statistics.

## Static GitHub Pages site

The existing `docs/` site is unchanged. To preview it locally:

```powershell
python -m http.server 8000 --directory docs
```

To deploy it, enable GitHub Pages for the repository and serve the `/docs` folder from the `main` branch.
