# Anu A - 3D Portfolio (Python + Streamlit)

An interactive 3D portfolio: a Three.js hero scene that reacts to your mouse and scroll,
a draggable 3D skills globe, and tilting project cards.

## Folder map

| File | What it is | Do you edit it? |
|------|------------|-----------------|
| `portfolio_data.py` | ALL your content, links and colours | **Yes, this is the main one** |
| `assets/` | Your photo and resume PDF | Replace files, keep the names (or change them in `portfolio_data.py`) |
| `template/portfolio.html` | Layout, styling, 3D scene | Only to change the design |
| `app.py` | Streamlit launcher | No |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customise

- **Text, projects, skills, certificates, links:** edit `portfolio_data.py`.
- **Add a project:** copy one `{...}` block inside `PROJECTS` and change it. Paste your GitHub repo in `github` and a live link in `demo`.
- **Hide a section:** set its list to `[]`, e.g. `CERTIFICATIONS = []`.
- **Colours (including the 3D model):** change the hex codes in `THEME`.
- **New photo or resume:** replace `assets/anu-profile.jpg` / `assets/resume.pdf`.
- **3D model speed or shape:** open `template/portfolio.html`, search for `Three.js hero scene`.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repo and push this folder:
   ```bash
   git init
   git add .
   git commit -m "3D portfolio"
   git branch -M main
   git remote add origin https://github.com/anu-2024/portfolio.git
   git push -u origin main
   ```
2. Go to https://share.streamlit.io, sign in with GitHub and click **Create app**.
3. Choose the repo, branch `main`, main file path `app.py`, then **Deploy**.
4. Every later edit you push to GitHub updates the live site.

## Notes

- The 3D scene loads Three.js and the fonts from a CDN, so the page needs internet access. If they are blocked, the site still works without the 3D background.
- The contact form opens the visitor's email app (Streamlit has no mail server). 
