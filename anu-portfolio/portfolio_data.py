"""
=====================================================================
  EDIT THIS FILE TO UPDATE YOUR PORTFOLIO
  Everything shown on the website comes from here.
  After saving, Streamlit reloads and the site updates.
  Tip: set a section's list to [] (empty) and that section disappears.
=====================================================================
"""

# ---------------------------------------------------------------
# 1. FILES  (put your own files inside the /assets folder)
# ---------------------------------------------------------------
PHOTO_FILE = "assets/anu-profile.jpg"   # your profile photo
RESUME_FILE = "assets/resume.pdf"       # shown as "Download resume" button
RESUME_DOWNLOAD_NAME = "Anu_A_Resume.pdf"

# ---------------------------------------------------------------
# 2. BROWSER TAB
# ---------------------------------------------------------------
PAGE_TITLE = "Anu A | Generative AI & Python Developer"
PAGE_ICON = "🌐"

# ---------------------------------------------------------------
# 3. COLOURS  (any hex code)
# ---------------------------------------------------------------
THEME = {
    "bg": "#0C1024",        # page background
    "panel": "#151B3B",     # cards
    "text": "#EEF0FF",      # main text
    "muted": "#9AA3C7",     # secondary text
    "accent": "#8C7BFF",    # main highlight (buttons, 3D gem)
    "accent2": "#4FE3D0",   # second highlight (3D nodes, links)
}

# ---------------------------------------------------------------
# 4. ABOUT YOU
# ---------------------------------------------------------------
PROFILE = {
    "name": "Anu A",
    "greeting": "Hi, I'm",
    "headline": "I build AI agents and data apps that solve real problems.",
    "subline": "MCA student specialising in Generative AI, Bangalore",
    "summary": (
        "MCA student specialising in Generative AI with hands-on experience in "
        "Python, AI agents, prompt engineering, machine learning and application "
        "development. I enjoy building AI-powered and data-driven projects with "
        "Python, Streamlit and SQL, and I'm interested in LLM application "
        "development, REST API integration, agent evaluation and deploying "
        "reliable AI solutions for real business problems."
    ),
    # Extra paragraphs shown in the About section (add / remove freely)
    "about": [
        "I'm pursuing my Master of Computer Applications at Alliance University, "
        "Bangalore. Alongside my studies I worked as an IT trainer, teaching Python, "
        "Java, C and C++, which sharpened how clearly I explain technical ideas.",
        "I learn quickly, enjoy solving problems, and like turning an idea into "
        "something people can open and use, from an AI shopping assistant to an "
        "eco-friendly route planner.",
    ],
    "location": "Bangalore",
    "email": "connectwithmeanu@gmail.com",   # the only contact shown on the site
    "available_for": "Open to internships and entry-level roles in AI, Python and data.",
}

# Big numbers in the About section
STATS = [
    ("8.4", "MCA CGPA (till Sem 3)"),
    ("4", "Projects built"),
    ("9", "Certifications"),
    ("3", "Internships and roles"),
]

# Social / profile links  (label, url)  - leave url "" to hide
LINKS = [
    ("GitHub", "https://github.com/anu-2024"),
    ("LinkedIn", "https://www.linkedin.com/in/anu-a-"),
    ("LeetCode", "https://leetcode.com/u/Anu_A_2"),
    ("HackerRank", "https://www.hackerrank.com/profile/anuanjenappa"),
]

# ---------------------------------------------------------------
# 5. SKILLS
#    Each group becomes a tab in the "Toolkit" section. Add / rename freely.
# ---------------------------------------------------------------
SKILL_GROUPS = {
    "Languages": ["Python", "Java", "C", "C++", "JavaScript", "TypeScript"],
    "Generative AI": ["Gemini", "Google AI Studio", "AI Agents", "Prompt Engineering", "Agent Development Kit"],
    "Data and ML": ["NumPy", "Pandas", "Matplotlib", "Plotly", "Scikit-learn"],
    "Web and APIs": ["Streamlit", "Django", "FastAPI", "Spring Boot", "React", "HTML", "CSS"],
    "Databases": ["MySQL", "SQLite", "MongoDB"],
    "Tools": ["Git and GitHub", "VS Code", "Docker", "Hugging Face", "Figma"],
}

# ---------------------------------------------------------------
# 6. EXPERIENCE  (newest first)
# ---------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Intern, 1M1B Green Skills Academy",
        "org": "In partnership with AICTE, supported by Salesforce",
        "period": "Feb 2026 to Mar 2026",
        "place": "Remote",
        "link": "https://drive.google.com/file/d/1nEKeYbR2Vpk-RiZT3T96lQ85oylpLj9E/view?usp=sharing",
        "link_label": "View certificate",
        "points": [
            "Implemented distance-based emission calculations and data processing for travel routes.",
            "Built interactive visualisations with Pandas, Streamlit and Plotly to support environmentally responsible travel decisions.",
        ],
    },
    {
        "role": "IT Trainer",
        "org": "CCSI Computer Education",
        "period": "Apr 2025 to Nov 2025",
        "place": "Bangalore, India",
        "points": [
            "Conducted programming sessions in Python, Java, C and C++.",
            "Gave practical coding guidance and supported students with their projects.",
        ],
    },
    {
        "role": "Intern",
        "org": "Academor",
        "period": "Feb 2024 to Mar 2024",
        "place": "Remote",
        "points": [
            "Used Python, Pandas, NumPy, Scikit-learn and Matplotlib for data preprocessing, exploratory analysis, model development and visualisation on real-world datasets.",
        ],
    },
]

# ---------------------------------------------------------------
# 7. PROJECTS
#    github: repo URL.  demo: live-app URL.  Leave "" to hide that button.
# ---------------------------------------------------------------
PROJECTS = [
    {
        "title": "CymbalMart Shopping Agent",
        "description": "An AI shopping assistant that turns natural-language event requirements into personalised, budget-conscious product recommendations and curated shopping carts.",
        "stack": ["Google AI Studio", "Gemini", "React", "TypeScript"],
        "github": "https://github.com/anu-2024/CymbalMart-Shopping-Agent",
        "demo": "",
    },
    {
        "title": "Smart Waste Management",
        "description": "A waste-management environment exposed through a FastAPI service with Pydantic models, containerised with Docker and deployed on Hugging Face Spaces.",
        "stack": ["Python", "FastAPI", "OpenEnv Framework", "Hugging Face Spaces", "Docker", "Pydantic"],
        "github": "https://github.com/anu-2024/smart-waste-openenv",
        "demo": "",
    },
    {
        "title": "Green Route Travel Recommendation System",
        "description": "An eco-friendly route recommender for Indian cities that uses machine learning models and route optimisation to suggest lower-emission journeys.",
        "stack": ["Python", "Machine Learning", "Streamlit"],
        "github": "https://github.com/anu-2024/GR-TRAVEL-RECOMMENDATION-",
        "demo": "",
    },
    {
        "title": "Community Resource Sharing System",
        "description": "A platform where people donate or request unused household items, encouraging resource sharing within communities.",
        "stack": ["Java Spring Boot", "Streamlit", "SQLite"],
        "github": "https://github.com/anu-2024/Community-Resource-Sharing-System",
        "demo": "",
    },
]

# ---------------------------------------------------------------
# 8. EDUCATION  (newest first)
# ---------------------------------------------------------------
EDUCATION = [
    {
        "degree": "Master of Computer Applications (MCA)",
        "school": "Alliance University, Bangalore, Karnataka",
        "period": "2025 to 2027",
        "score": "CGPA 8.4 till Semester 3 (Sem 1: 8.5, Sem 2: 8.2)",
    },
    {
        "degree": "Bachelor of Computer Applications (BCA)",
        "school": "St Francis De Sales College, Bangalore, Karnataka",
        "period": "2021 to 2024",
        "score": "79.26% (CGPA 7.9)",
    },
    {
        "degree": "HSC (Pre-University)",
        "school": "Swamy Vivekananda PU College, Karnataka",
        "period": "2021",
        "score": "78.83%",
    },
    {
        "degree": "SSLC",
        "school": "Shree Ananthanagar Vidyaniketan High School, Karnataka",
        "period": "2019",
        "score": "75.52%",
    },
]

# ---------------------------------------------------------------
# 9. CERTIFICATIONS  (name, issuer, certificate link - "" to hide the link)
# ---------------------------------------------------------------
CERTIFICATIONS = [
    ("Engineer AI Agents with Agent Development Kit (ADK)", "Google",
     "https://www.credly.com/badges/d592ebc9-5315-414d-84f8-efcb3c16bd67/linked_in?t=tfut7r"),
    ("Applied Generative AI Certification", "Infosys Springboard",
     "https://drive.google.com/file/d/1u1l8gbHlXD4XlukghrrQe4Ze2qXGY4re/view?usp=sharing"),
    ("Data Analysis with Python", "IBM",
     "https://www.coursera.org/account/accomplishments/records/YMHZ9GP1QI0J"),
    ("Java Programming for Beginners", "IBM",
     "https://www.coursera.org/account/accomplishments/verify/ZRIPZOGN6M2Z"),
    ("Introduction to Databases", "Meta",
     "https://www.coursera.org/account/accomplishments/verify/EDVCRN535ABF"),
    ("Introduction to Front End Development", "Meta",
     "https://www.coursera.org/account/accomplishments/records/OADY2FNTVIFE"),
    ("User Interface Design and Prototyping", "Microsoft",
     "https://www.coursera.org/account/accomplishments/records/DXG57J5TU9GE"),
    ("Advanced Data Structures and Algorithms", "Packt",
     "https://www.coursera.org/account/accomplishments/verify/KA89QRVZ2NB5"),
    ("Applied Statistics for Data Analytics", "DeepLearning.AI",
     "https://www.coursera.org/account/accomplishments/verify/I0D2YVV0GCGL"),
]

# ---------------------------------------------------------------
# 10. LEADERSHIP & ACHIEVEMENTS
# ---------------------------------------------------------------
ACHIEVEMENTS = [
    {
        "title": "Secretary, Rotaract Club",
        "text": "Served as Club Secretary for one year, streamlining official correspondence and record-keeping for a campus organisation of 50+ members to improve team communication.",
    },
]
