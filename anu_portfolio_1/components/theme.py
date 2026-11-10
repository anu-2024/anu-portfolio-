import streamlit as st

DARK_VARS = """
  --bg: #060913;
  --bg-2: #0a1020;
  --text: #f2f5ff;
  --text-soft: #c5cee2;
  --muted: #93a2bf;
  --panel: rgba(16, 24, 43, 0.82);
  --panel-2: rgba(10, 16, 31, 0.9);
  --panel-solid: #0f1729;
  --line: rgba(160, 180, 220, 0.16);
  --line-strong: rgba(160, 180, 220, 0.3);
  --violet: #9b8cff;
  --cyan: #65d8e8;
  --green: #5ee0a0;
  --amber: #f6c76b;
  --red: #ff7b89;
  --chip-bg: rgba(255, 255, 255, 0.035);
  --chip-bg-hover: rgba(255, 255, 255, 0.07);
  --grid-line: rgba(255, 255, 255, 0.032);
  --glow-violet: rgba(155, 140, 255, 0.22);
  --glow-cyan: rgba(101, 216, 232, 0.12);
  --input-bg: rgba(10, 16, 31, 0.82);
  --shadow: 0 24px 70px rgba(0, 0, 0, 0.34);
  --shadow-soft: 0 12px 36px rgba(0, 0, 0, 0.18);
  --ring: rgba(101, 216, 232, 0.18);
  --code-bg: #0b1222;
"""

LIGHT_VARS = """
  --bg: #f4f6fb;
  --bg-2: #eef2fa;
  --text: #111827;
  --text-soft: #374151;
  --muted: #5f6b7f;
  --panel: rgba(255, 255, 255, 0.86);
  --panel-2: rgba(247, 249, 254, 0.92);
  --panel-solid: #ffffff;
  --line: rgba(15, 23, 42, 0.13);
  --line-strong: rgba(15, 23, 42, 0.24);
  --violet: #6b5ce7;
  --cyan: #0d94a8;
  --green: #0f9f6e;
  --amber: #a86c00;
  --red: #c24155;
  --chip-bg: rgba(15, 23, 42, 0.035);
  --chip-bg-hover: rgba(15, 23, 42, 0.07);
  --grid-line: rgba(15, 23, 42, 0.045);
  --glow-violet: rgba(107, 92, 231, 0.12);
  --glow-cyan: rgba(13, 148, 168, 0.08);
  --input-bg: rgba(255, 255, 255, 0.92);
  --shadow: 0 24px 70px rgba(31, 41, 55, 0.12);
  --shadow-soft: 0 12px 36px rgba(31, 41, 55, 0.08);
  --ring: rgba(13, 148, 168, 0.16);
  --code-bg: #eef2fa;
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  __VARS__
  --font-body: 'Manrope', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-mono: 'DM Mono', 'Cascadia Code', Consolas, monospace;
}

html {
  scroll-behavior: smooth;
}

html, body, [class*="css"] {
  font-family: var(--font-body);
}

.stApp {
  color: var(--text);
  background:
    radial-gradient(circle at 82% -8%, var(--glow-violet), transparent 34%),
    radial-gradient(circle at 2% 28%, var(--glow-cyan), transparent 30%),
    linear-gradient(var(--grid-line) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-line) 1px, transparent 1px),
    var(--bg);
  background-size: auto, auto, 64px 64px, 64px 64px, auto;
  background-attachment: fixed;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
footer {
  display: none !important;
}

[data-testid="stAppViewContainer"] {
  background: transparent;
}

.block-container {
  max-width: 1240px;
  padding: 1.2rem 2.4rem 4.5rem;
  position: relative;
  z-index: 1;
}

.stApp p,
.stApp li {
  color: var(--text-soft);
  line-height: 1.75;
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
  color: var(--text);
  letter-spacing: -0.04em;
}

.stApp a {
  color: var(--cyan);
  text-decoration: none;
}

.stApp a:hover {
  color: var(--violet);
}

::selection {
  background: var(--violet);
  color: #07101f;
}

::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--line-strong);
  border-radius: 999px;
}

a:focus-visible,
button:focus-visible {
  outline: 2px solid var(--cyan);
  outline-offset: 3px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.2rem;
  flex-wrap: wrap;
  padding: 0.35rem 0 1rem;
  margin-bottom: 0.2rem;
  border-bottom: 1px solid var(--line);
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.7rem;
  color: var(--text) !important;
  font-weight: 800;
  letter-spacing: -0.04em;
  font-size: 1.05rem;
}

.brand-mark {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--violet), var(--cyan));
  color: #07101f;
  font-weight: 800;
  box-shadow: 0 8px 24px var(--ring);
}

.brand small {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.grad {
  background: linear-gradient(100deg, var(--violet), var(--cyan));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.05rem;
  flex-wrap: wrap;
}

.nav-links a {
  color: var(--muted);
  font-size: 0.8rem;
  font-weight: 600;
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: var(--text);
}

.nav-utils {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  padding: 0.48rem 0.75rem;
  background: var(--chip-bg);
  color: var(--text) !important;
  font-size: 0.72rem;
  font-weight: 700;
  transition: border-color 0.2s ease, background 0.2s ease, transform 0.2s ease;
}

.nav-pill:hover {
  border-color: var(--cyan);
  background: var(--chip-bg-hover);
  transform: translateY(-1px);
}

.nav-pill.primary {
  background: linear-gradient(100deg, var(--violet), var(--cyan));
  border-color: transparent;
  color: #07101f !important;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(300px, 0.88fr);
  gap: 3rem;
  align-items: center;
  padding: 4.4rem 0 3.6rem;
}

.hero-copy {
  min-width: 0;
}

.status {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  border: 1px solid var(--line-strong);
  background: var(--chip-bg);
  border-radius: 999px;
  padding: 0.45rem 0.7rem;
  color: var(--text-soft);
  font-family: var(--font-mono);
  font-size: 0.64rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 0 4px rgba(94, 224, 160, 0.12);
  animation: pulse 2.4s ease-in-out infinite;
}

.eyebrow {
  color: var(--cyan);
  font-family: var(--font-mono);
  font-size: 0.64rem;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.hero .eyebrow {
  margin-top: 1.4rem;
}

.hero h1 {
  font-size: clamp(3rem, 6.4vw, 6.1rem);
  line-height: 0.96;
  letter-spacing: -0.07em;
  margin: 0.8rem 0 1.2rem;
}

.hero h1 .line {
  display: block;
}

.hero .lead {
  max-width: 640px;
  color: var(--muted);
  font-size: 1.05rem;
  line-height: 1.85;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin: 1.6rem 0 1.8rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  border-radius: 999px;
  padding: 0.72rem 1.05rem;
  font-size: 0.82rem;
  font-weight: 700;
  border: 1px solid transparent;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease, color 0.2s ease;
}

.btn-primary {
  background: linear-gradient(100deg, var(--violet), var(--cyan));
  color: #07101f !important;
  box-shadow: 0 12px 30px var(--ring);
}

.btn-primary:hover {
  color: #07101f !important;
  transform: translateY(-2px);
}

.btn-ghost {
  border-color: var(--line-strong);
  background: var(--chip-bg);
  color: var(--text) !important;
}

.btn-ghost:hover {
  border-color: var(--cyan);
  color: var(--cyan) !important;
  transform: translateY(-2px);
}

.stat-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.7rem;
  max-width: 680px;
}

.stat {
  border-top: 1px solid var(--line);
  padding-top: 0.75rem;
}

.stat strong {
  display: block;
  color: var(--text);
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -0.04em;
}

.stat span {
  color: var(--muted);
  font-size: 0.7rem;
  font-family: var(--font-mono);
  letter-spacing: 0.02em;
}

.hero-visual {
  position: relative;
  min-width: 0;
}

.portrait-frame {
  position: relative;
  border-radius: 34px;
  padding: 5px;
  background: linear-gradient(140deg, var(--violet), var(--cyan));
  box-shadow: var(--shadow);
}

.portrait-frame::after {
  content: "";
  position: absolute;
  inset: 14%;
  border-radius: 50%;
  background: var(--glow-violet);
  filter: blur(50px);
  z-index: -1;
}

.portrait-frame img {
  display: block;
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 30px;
}

.portrait-placeholder {
  display: grid;
  place-items: center;
  aspect-ratio: 1;
  border-radius: 30px;
  background: var(--panel-solid);
  color: var(--muted);
  font-size: 2rem;
  font-weight: 800;
}

.float-chip {
  position: absolute;
  z-index: 2;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  border: 1px solid var(--line-strong);
  background: var(--panel);
  backdrop-filter: blur(16px);
  border-radius: 14px;
  padding: 0.55rem 0.75rem;
  color: var(--text);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.02em;
  box-shadow: var(--shadow-soft);
  animation: float 7s ease-in-out infinite;
}

.float-chip.one {
  top: 8%;
  left: -8%;
}

.float-chip.two {
  bottom: 9%;
  right: -7%;
  animation-delay: -2.4s;
}

.float-chip .dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--cyan);
}

.float-chip .dot.violet {
  background: var(--violet);
}

.marquee {
  overflow: hidden;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding: 0.85rem 0;
  margin-top: 0.4rem;
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.marquee-track {
  display: flex;
  width: max-content;
  animation: marquee 34s linear infinite;
}

.marquee-group {
  display: flex;
  align-items: center;
  gap: 2.1rem;
  padding-right: 2.1rem;
}

.marquee-item {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  white-space: nowrap;
}

.marquee-dot {
  color: var(--cyan);
}

.section {
  padding: 4.4rem 0 0.6rem;
}

.section-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1.5rem;
  padding-top: 4.4rem;
  margin-bottom: 1.7rem;
}

.section-head.compact {
  padding-top: 2.4rem;
}

.section-head h2 {
  font-size: clamp(1.85rem, 3.5vw, 2.9rem);
  line-height: 1.04;
  margin: 0.35rem 0 0;
}

.section-head p {
  max-width: 520px;
  margin: 0;
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.75;
}

.section-head .eyebrow {
  display: block;
}

.panel {
  background: linear-gradient(145deg, var(--panel), var(--panel-2));
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 1.45rem;
  box-shadow: var(--shadow-soft);
  backdrop-filter: blur(14px);
}

.about-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr);
  gap: 1.1rem;
}

.about-copy p {
  margin: 0 0 1rem;
  color: var(--text-soft);
  font-size: 0.94rem;
  line-height: 1.85;
}

.about-copy p:last-child {
  margin-bottom: 0;
}

.focus-list {
  display: grid;
  gap: 0.7rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.focus-list li {
  display: flex;
  gap: 0.8rem;
  align-items: flex-start;
  color: var(--text-soft);
  font-size: 0.86rem;
  line-height: 1.55;
}

.focus-list .num {
  color: var(--cyan);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.08em;
  padding-top: 0.15rem;
}

.mini-education {
  margin-top: 1.2rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--line);
}

.mini-education strong {
  display: block;
  color: var(--text);
  font-size: 0.88rem;
}

.mini-education span {
  display: block;
  color: var(--muted);
  font-size: 0.76rem;
  margin-top: 0.2rem;
}

.skill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.skill-card {
  display: flex;
  flex-direction: column;
  min-height: 210px;
}

.skill-icon {
  width: 40px;
  height: 40px;
  border-radius: 13px;
  display: grid;
  place-items: center;
  color: var(--violet);
  background: var(--chip-bg);
  border: 1px solid var(--line);
}

.skill-icon svg {
  width: 20px;
  height: 20px;
}

.skill-card h3 {
  margin: 0.85rem 0 0.35rem;
  font-size: 1.02rem;
}

.skill-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.8rem;
  line-height: 1.65;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.38rem;
  margin-top: 0.85rem;
}

.chip {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  background: var(--chip-bg);
  border-radius: 999px;
  padding: 0.3rem 0.52rem;
  color: var(--text-soft);
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.02em;
}

.skill-related {
  margin-top: auto;
  padding-top: 1rem;
  color: var(--muted);
  font-size: 0.72rem;
  line-height: 1.55;
}

.skill-related a {
  color: var(--cyan);
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.1rem;
}

.project-card {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 24px;
  background: linear-gradient(160deg, var(--panel), var(--panel-2));
  box-shadow: var(--shadow-soft);
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent);
  box-shadow: 0 22px 60px var(--accent-soft);
}

.project-cover {
  position: relative;
  height: 172px;
  overflow: hidden;
  background:
    radial-gradient(circle at 82% 18%, var(--accent-soft), transparent 44%),
    linear-gradient(135deg, var(--accent-soft), var(--panel-2));
}

.project-cover::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.07) 1px, transparent 1px);
  background-size: 28px 28px;
  opacity: 0.55;
  mask-image: linear-gradient(180deg, #000, transparent);
  -webkit-mask-image: linear-gradient(180deg, #000, transparent);
}

.project-cover::after {
  content: "";
  position: absolute;
  width: 210px;
  height: 210px;
  border-radius: 50%;
  right: -55px;
  top: -85px;
  background: var(--accent-soft);
  filter: blur(14px);
}

.cover-tag,
.cover-index {
  position: absolute;
  z-index: 1;
  top: 1rem;
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.cover-tag {
  left: 1rem;
  color: var(--text);
  border: 1px solid var(--line-strong);
  background: var(--panel);
  backdrop-filter: blur(8px);
  border-radius: 999px;
  padding: 0.32rem 0.55rem;
}

.cover-index {
  right: 1rem;
  color: var(--muted);
}

.cover-glyph {
  position: absolute;
  z-index: 1;
  right: 1.15rem;
  bottom: 0.65rem;
  color: var(--accent);
  font-size: 3.4rem;
  font-weight: 800;
  letter-spacing: -0.09em;
  opacity: 0.92;
}

.project-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 1.15rem 1.25rem 1.25rem;
}

.project-kicker {
  color: var(--cyan);
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
}

.project-card h3 {
  margin: 0.45rem 0 0.55rem;
  font-size: 1.15rem;
  line-height: 1.25;
}

.project-card h3 a {
  color: var(--text);
}

.project-card h3 a:hover {
  color: var(--cyan);
}

.project-summary {
  margin: 0;
  color: var(--muted);
  font-size: 0.82rem;
  line-height: 1.68;
  flex: 1;
}

.project-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.8rem;
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.6rem;
}

.project-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.85rem;
  margin-top: 1rem;
  padding-top: 0.85rem;
  border-top: 1px solid var(--line);
}

.card-link {
  color: var(--cyan) !important;
  font-size: 0.74rem;
  font-weight: 700;
}

.card-link:hover {
  color: var(--violet) !important;
}

.card-link.muted {
  color: var(--muted) !important;
}

.case-study-wrap {
  position: relative;
}

.case-study-empty {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  border: 1px dashed var(--line-strong);
  border-radius: 18px;
  padding: 1.1rem 1.2rem;
  color: var(--muted);
  font-size: 0.82rem;
}

.case-study-empty .arrow {
  color: var(--cyan);
  font-size: 1.1rem;
}

.case-study-wrap:has(.project-detail:target) .case-study-empty {
  display: none;
}

.project-detail {
  display: none;
  scroll-margin-top: 30px;
}

.project-detail:target {
  display: block;
  animation: fadeUp 0.5s ease both;
}

.detail-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.9rem;
}

.detail-back {
  color: var(--cyan) !important;
  font-size: 0.74rem;
  font-weight: 700;
}

.detail-index {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.08em;
}

.detail-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(260px, 0.65fr);
  gap: 1.1rem;
}

.detail-main h2 {
  font-size: clamp(1.8rem, 3.4vw, 2.6rem);
  margin: 0.35rem 0 0.8rem;
  line-height: 1.05;
}

.detail-main p {
  color: var(--text-soft);
  font-size: 0.9rem;
  line-height: 1.8;
}

.detail-main h3 {
  margin: 1.25rem 0 0.45rem;
  font-size: 0.92rem;
}

.detail-list {
  margin: 0;
  padding-left: 1.1rem;
  color: var(--text-soft);
  font-size: 0.86rem;
  line-height: 1.7;
}

.detail-list li {
  margin-bottom: 0.35rem;
}

.detail-side {
  align-self: start;
}

.detail-side h4 {
  margin: 0 0 0.55rem;
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.11em;
  text-transform: uppercase;
}

.detail-side .chips {
  margin-top: 0;
}

.detail-side .detail-links {
  display: grid;
  gap: 0.55rem;
  margin-top: 1.1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.language-list {
  display: grid;
  gap: 0.45rem;
  margin-top: 1rem;
}

.language-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.5rem;
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.6rem;
}

.experience-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(260px, 0.65fr);
  gap: 1.1rem;
}

.timeline {
  position: relative;
  padding-left: 1.35rem;
  border-left: 1px solid var(--line);
}

.timeline-item {
  position: relative;
  padding: 0 0 1.35rem 1.15rem;
}

.timeline-item:last-child {
  padding-bottom: 0;
}

.timeline-item::before {
  content: "";
  position: absolute;
  left: -1.42rem;
  top: 0.42rem;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--cyan);
  box-shadow: 0 0 0 4px var(--ring);
}

.timeline-meta {
  color: var(--cyan);
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.timeline-item h3 {
  margin: 0.35rem 0 0.2rem;
  font-size: 1.02rem;
}

.timeline-org {
  color: var(--muted);
  font-size: 0.76rem;
  margin-bottom: 0.45rem;
}

.timeline-item p {
  margin: 0;
  color: var(--text-soft);
  font-size: 0.82rem;
  line-height: 1.7;
}

.timeline-item .chips {
  margin-top: 0.65rem;
}

.leadership-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.3fr) minmax(260px, 0.7fr);
  gap: 1.1rem;
}

.leadership-feature {
  position: relative;
  overflow: hidden;
  padding: 1.8rem;
  background:
    radial-gradient(circle at 100% 0%, var(--glow-violet), transparent 36%),
    linear-gradient(145deg, var(--panel), var(--panel-2));
}

.leadership-mark {
  width: 54px;
  height: 54px;
  border-radius: 17px;
  display: grid;
  place-items: center;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--violet), var(--cyan));
  color: #07101f;
  font-weight: 800;
  letter-spacing: -0.04em;
  box-shadow: 0 10px 28px var(--ring);
}

.leadership-feature h2 {
  margin: 0.35rem 0 0.2rem;
  font-size: clamp(1.8rem, 3.2vw, 2.6rem);
  line-height: 1.05;
}

.leadership-org {
  color: var(--muted);
  font-size: 0.82rem;
  margin-bottom: 0.7rem;
}

.leadership-feature p {
  margin: 0;
  color: var(--text-soft);
  font-size: 0.88rem;
  line-height: 1.75;
}

.leadership-side {
  align-self: start;
}

.education-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.education-card {
  position: relative;
  overflow: hidden;
}

.education-card .year {
  color: var(--violet);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.1em;
}

.education-card h3 {
  margin: 0.55rem 0 0.35rem;
  font-size: 1.1rem;
}

.education-card .institution {
  color: var(--text-soft);
  font-size: 0.84rem;
}

.education-card .location {
  color: var(--muted);
  font-size: 0.74rem;
  margin-top: 0.2rem;
}

.education-card .note {
  margin: 0.9rem 0 0;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1.65;
}

.cert-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 0.8rem;
}

.cert-card {
  display: flex;
  gap: 0.8rem;
  align-items: flex-start;
  padding: 1rem;
}

.cert-badge {
  flex: 0 0 auto;
  width: 36px;
  height: 36px;
  border-radius: 11px;
  display: grid;
  place-items: center;
  background: var(--chip-bg);
  border: 1px solid var(--line);
  color: var(--cyan);
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 500;
}

.cert-card h3 {
  margin: 0;
  font-size: 0.84rem;
  line-height: 1.45;
}

.cert-card p {
  margin: 0.25rem 0 0;
  color: var(--muted);
  font-size: 0.7rem;
}

.metric-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.8rem;
  margin-bottom: 1.1rem;
}

.metric-card {
  padding: 1rem 1.1rem;
}

.metric-card strong {
  display: block;
  color: var(--text);
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.05em;
}

.metric-card span {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.6rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.github-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.github-note {
  color: var(--muted);
  font-size: 0.74rem;
  line-height: 1.6;
}

.github-grid {
  display: grid;
  grid-template-columns: minmax(0, 0.36fr) minmax(0, 0.64fr);
  gap: 1.1rem;
  align-items: start;
}

.language-bars {
  display: grid;
  gap: 0.55rem;
}

.language-line {
  display: grid;
  grid-template-columns: 108px minmax(0, 1fr) 46px;
  gap: 0.6rem;
  align-items: center;
}

.language-line .name {
  color: var(--text-soft);
  font-size: 0.7rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.language-line .value {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.58rem;
  text-align: right;
}

.lang-track {
  height: 7px;
  border-radius: 999px;
  background: var(--chip-bg);
  overflow: hidden;
}

.lang-fill {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--violet), var(--cyan));
}

.repo-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.8rem;
}

.repo-card {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.repo-card h3 {
  margin: 0.35rem 0 0.35rem;
  font-size: 0.9rem;
  line-height: 1.35;
}

.repo-card h3 a {
  color: var(--text);
}

.repo-card h3 a:hover {
  color: var(--cyan);
}

.repo-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.74rem;
  line-height: 1.6;
  flex: 1;
}

.repo-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.75rem;
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.58rem;
}

.repo-link {
  margin-top: 0.75rem;
  color: var(--cyan) !important;
  font-size: 0.72rem;
  font-weight: 700;
}

.error-panel {
  display: flex;
  align-items: flex-start;
  gap: 0.8rem;
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1.1rem 1.2rem;
  background: var(--panel);
}

.error-panel .glyph {
  color: var(--amber);
  font-size: 1.1rem;
}

.error-panel strong {
  display: block;
  color: var(--text);
  font-size: 0.86rem;
  margin-bottom: 0.2rem;
}

.error-panel p {
  margin: 0;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1.6;
}

.recruiter-card {
  position: relative;
  overflow: hidden;
  padding: 1.8rem;
  background:
    radial-gradient(circle at 100% 0%, var(--glow-violet), transparent 34%),
    linear-gradient(145deg, var(--panel), var(--panel-2));
}

.recruiter-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
  gap: 1.6rem;
}

.recruiter-card h2 {
  font-size: clamp(1.7rem, 3vw, 2.4rem);
  line-height: 1.05;
  margin: 0.35rem 0 0.8rem;
}

.recruiter-card p {
  color: var(--text-soft);
  font-size: 0.88rem;
  line-height: 1.75;
}

.recruiter-facts {
  display: grid;
  gap: 0.7rem;
  margin-top: 1.1rem;
}

.fact-row {
  display: grid;
  grid-template-columns: 104px minmax(0, 1fr);
  gap: 0.7rem;
  padding-bottom: 0.65rem;
  border-bottom: 1px solid var(--line);
}

.fact-row:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.fact-row span {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.58rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fact-row strong {
  color: var(--text);
  font-size: 0.78rem;
  font-weight: 600;
  line-height: 1.5;
}

.role-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  margin-top: 1rem;
}

.faq-shell {
  display: grid;
  grid-template-columns: minmax(0, 0.32fr) minmax(0, 0.68fr);
  gap: 1.1rem;
  align-items: start;
}

.faq-side h3 {
  margin: 0.35rem 0 0.55rem;
  font-size: 1.1rem;
}

.faq-side p {
  margin: 0;
  color: var(--muted);
  font-size: 0.8rem;
  line-height: 1.7;
}

.faq-note {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.7rem;
  line-height: 1.6;
}

.contact-card {
  position: relative;
  overflow: hidden;
  padding: 1.9rem;
  background:
    radial-gradient(circle at 8% 0%, var(--glow-cyan), transparent 32%),
    radial-gradient(circle at 95% 10%, var(--glow-violet), transparent 36%),
    linear-gradient(145deg, var(--panel), var(--panel-2));
}

.contact-card h2 {
  font-size: clamp(2rem, 4vw, 3.4rem);
  line-height: 1.02;
  letter-spacing: -0.06em;
  margin: 0.4rem 0 0.8rem;
  max-width: 780px;
}

.contact-card p {
  max-width: 680px;
  color: var(--text-soft);
  font-size: 0.92rem;
  line-height: 1.75;
}

.contact-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 1.35rem;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 0.7rem;
  margin-top: 1.4rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
}

.contact-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.contact-item span {
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.58rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.contact-item a,
.contact-item strong {
  color: var(--text);
  font-size: 0.82rem;
  font-weight: 600;
  word-break: break-word;
}

.contact-item a:hover {
  color: var(--cyan);
}

.footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: 2.4rem 0 0.5rem;
  margin-top: 2.2rem;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.72rem;
}

.footer a {
  color: var(--muted);
}

.footer a:hover {
  color: var(--cyan);
}

.anchor {
  scroll-margin-top: 28px;
}

[data-testid="stMarkdownContainer"] > div:has(> .section-anchor) {
  height: 0;
}

div[data-testid="stChatMessage"] {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 0.9rem 1rem;
  margin-bottom: 0.55rem;
}

div[data-testid="stChatMessage"] p {
  color: var(--text-soft);
  font-size: 0.84rem;
  line-height: 1.7;
}

div[data-testid="stForm"] {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1rem;
}

div[data-baseweb="input"],
div[data-baseweb="textarea"] {
  background: var(--input-bg) !important;
  border-color: var(--line) !important;
  border-radius: 12px !important;
}

input,
textarea {
  color: var(--text) !important;
  caret-color: var(--cyan) !important;
}

input::placeholder,
textarea::placeholder {
  color: var(--muted) !important;
}

.stButton > button,
[data-testid="stDownloadButton"] button {
  border-radius: 999px;
  border: 1px solid var(--line-strong);
  background: var(--chip-bg);
  color: var(--text);
  font-weight: 700;
  font-size: 0.78rem;
  padding: 0.5rem 0.95rem;
  transition: border-color 0.2s ease, color 0.2s ease, background 0.2s ease, transform 0.2s ease;
}

.stButton > button:hover,
[data-testid="stDownloadButton"] button:hover {
  border-color: var(--cyan);
  color: var(--cyan);
  background: var(--chip-bg-hover);
  transform: translateY(-1px);
}

.stButton > button:focus:not(:active),
[data-testid="stDownloadButton"] button:focus:not(:active) {
  border-color: var(--cyan);
  color: var(--cyan);
}

[data-testid="stCaptionContainer"] {
  color: var(--muted);
}

[data-testid="stAlert"] {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  color: var(--text-soft);
}

[data-testid="stSpinner"] {
  color: var(--cyan);
}

code {
  background: var(--code-bg);
  color: var(--cyan);
  border-radius: 6px;
  padding: 0.1rem 0.3rem;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(14px); }
  to { opacity: 1; transform: none; }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.55; transform: scale(0.82); }
}

@media (max-width: 1050px) {
  .hero {
    gap: 2rem;
  }

  .repo-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 980px) {
  .hero,
  .about-grid,
  .experience-grid,
  .education-grid,
  .leadership-grid,
  .detail-grid,
  .recruiter-grid,
  .github-grid,
  .faq-shell {
    grid-template-columns: 1fr;
  }

  .hero {
    padding-top: 3.2rem;
  }

  .hero-visual {
    max-width: 520px;
    margin: 0 auto;
    width: 100%;
  }

  .project-grid {
    grid-template-columns: 1fr;
  }

  .section-head {
    align-items: flex-start;
    flex-direction: column;
    gap: 0.8rem;
  }

  .metric-row {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .float-chip.one {
    left: -4%;
  }

  .float-chip.two {
    right: -3%;
  }
}

@media (max-width: 760px) {
  .block-container {
    padding: 0.85rem 1rem 3rem;
  }

  .topbar {
    gap: 0.7rem;
  }

  .nav-links {
    order: 3;
    width: 100%;
    overflow-x: auto;
    flex-wrap: nowrap;
    gap: 0.95rem;
    padding-bottom: 0.15rem;
    scrollbar-width: none;
  }

  .nav-links::-webkit-scrollbar {
    display: none;
  }

  .nav-utils {
    margin-left: auto;
  }

  .hero {
    padding: 2.6rem 0 2.6rem;
  }

  .hero h1 {
    font-size: clamp(2.55rem, 12vw, 4rem);
  }

  .hero .lead {
    font-size: 0.96rem;
  }

  .stat-row {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .float-chip {
    display: none;
  }

  .section {
    padding-top: 3.2rem;
  }

  .section-head {
    padding-top: 3.2rem;
  }

  .section-head.compact {
    padding-top: 1.8rem;
  }

  .project-cover {
    height: 150px;
  }

  .language-line {
    grid-template-columns: 88px minmax(0, 1fr) 42px;
  }

  .recruiter-card,
  .contact-card {
    padding: 1.25rem;
  }

  .fact-row {
    grid-template-columns: 88px minmax(0, 1fr);
  }
}

@media (max-width: 520px) {
  .hero-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .btn {
    width: 100%;
  }

  .metric-row {
    grid-template-columns: 1fr;
  }

  .stat-row {
    grid-template-columns: 1fr 1fr;
  }

  .contact-links {
    flex-direction: column;
    align-items: stretch;
  }

  .contact-links .btn {
    width: 100%;
  }

  .detail-top {
    align-items: flex-start;
    flex-direction: column;
    gap: 0.35rem;
  }

  .footer {
    align-items: flex-start;
    flex-direction: column;
  }
}

@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  *,
  *::before,
  *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
    scroll-behavior: auto !important;
  }
}
</style>
"""


def inject_styles(theme: str = "dark") -> None:
    variables = LIGHT_VARS if theme == "light" else DARK_VARS
    st.markdown(CSS.replace("__VARS__", variables), unsafe_allow_html=True)
