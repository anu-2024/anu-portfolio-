# Anu A — Living Developer Portfolio

A recruiter-first Streamlit portfolio with a premium dark visual system, curated project stories, experience, skills, downloadable resume and a live public GitHub repository feed.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Create a public GitHub repository (for example `anu-portfolio`).
2. Upload the contents of this ZIP to the repository root.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Select the repository, branch and `app.py` as the main file.
5. Deploy.

## GitHub auto-sync

The app calls the public GitHub REST API for `anu-2024` and caches results for 10 minutes. New public, non-fork repositories and changes to repository metadata appear in the live feed when a visitor reloads or reruns the app after the cache expires. The **Refresh GitHub data** button clears the cache and fetches immediately.

This is periodic API refresh, not a webhook or instant push notification. Streamlit Community Cloud apps are request/rerun driven, so a visitor refresh is needed to trigger a new fetch after the cache TTL. Public GitHub API rate limits apply.

Optional: add a GitHub personal access token in Streamlit Cloud → App → Settings → Secrets to increase API rate limits:

```toml
GITHUB_TOKEN = "your_token"
```

Use a fine-grained token with only public repository metadata access where possible. Never commit the token or `.streamlit/secrets.toml` to GitHub.

## Before publishing — important content checks

- Confirm that every curated project's repository URL points to the exact matching repository. The current curated cards link to the GitHub profile until exact repository names are verified.
- Confirm the Smart Waste Management project description and current implementation details.
- Confirm CGPA and dates in the resume. This draft uses the latest supplied technical resume's MCA CGPA of 8.4 (till Semester 3).
- Review contact details and resume PDF before making the repository public.
- Replace the resume PDF in `assets/` whenever your resume changes.

## Notes

- The portfolio assistant is a lightweight, rule-based FAQ using the supplied profile details. It does not send visitor questions to an external AI service.
- The website does not expose private GitHub repositories.
- The project cards intentionally separate curated work from the automatically populated repository feed.

## Verified curated repositories

The project cards now point to these confirmed public repositories:
- `CymbalMart-Shopping-Agent`
- `GR-TRAVEL-RECOMMENDATION-`
- `Community-Resource-Sharing-System`
- `AQI_Capstone_Project`
- `smart-waste-openenv`
- `VISUAL-SEARCH-WITH-OCR-COMPARISON-`
- `Emergency-Message-Prioritization-System`

Repository readmes were used to align the project summaries with their documented features and technology stacks. AgriNEWS was omitted because a matching public repository was not confirmed in the connected account's repository list.
