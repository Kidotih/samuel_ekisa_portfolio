import streamlit as st
from components import animated_intro, cta_buttons
from minigames import quiz_game, puzzle_game
from timeline import render_timeline
from analytics import render_analytics
from chatbot import chatbot
import json
from pathlib import Path
import time

# -----------------------
# Timeline Rendering Function
# -----------------------
# -----------------------
# Timeline Rendering Function (Compact Version)
# -----------------------
def render_timeline(experience_file):
    if not experience_file.exists():
        st.warning("Timeline file not found.")
        return

    with open(experience_file) as f:
        timeline = json.load(f)

    st.markdown("<h2 style='text-align:center; color:white;'>Timeline & Experience</h2>", unsafe_allow_html=True)
    st.markdown("<div style='position:relative; width:100%; margin-top:2rem;'>", unsafe_allow_html=True)

    for idx, item in enumerate(timeline):
        side = "left" if idx % 2 == 0 else "right"
        st.markdown(f"""
        <div style='width:45%; padding:1rem; background:#fff; color:#000; border-radius:10px; 
                    position:relative; margin:1rem 0; float:{side}; box-shadow:0 2px 8px rgba(0,0,0,0.2);
                    font-size:0.9rem;'>
            <h4 style='margin:0 0 0.3rem 0;'>{item.get('role','')} @ {item.get('company','')}</h4>
            <p style='margin:0 0 0.3rem 0; font-size:0.8rem; color:#555;'>{item.get('start','')} - {item.get('end','')}</p>
            <p style='margin:0;'>{item.get('description','')}</p>
            <div style='position:absolute; top:1rem; { "right:-10px" if side=="left" else "left:-10px" }; 
                        width:20px; height:20px; background:#fff; border:3px solid #00BFFF; border-radius:50%;'></div>
        </div>
        """, unsafe_allow_html=True)
    
    # Center vertical line
    st.markdown("""
    <div style='position:absolute; left:50%; top:0; bottom:0; width:4px; background:#00BFFF; margin-left:-2px;'></div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="Samuel Ekisa Portfolio", layout="wide")

# -----------------------
# Base Paths
# -----------------------
BASE_DIR = Path(__file__).resolve().parent      # app/
DATA_DIR = BASE_DIR.parent / "data"            # ../data/
PROJECTS_FILE = DATA_DIR / "projects.json"
EXPERIENCE_FILE = DATA_DIR / "experience.json"
SKILLS_FILE = DATA_DIR / "skills.json"

DATA_DIR = BASE_DIR / "data"    # not BASE_DIR.parent
EXPERIENCE_FILE = DATA_DIR / "experience.json"





# -----------------------
# Particle Background
# -----------------------
st.markdown("""
<div id="particles-js" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1;"></div>
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<script>
particlesJS("particles-js", {
  "particles": { "number": {"value":60}, "color":{"value":"#fff"}, "shape":{"type":"circle"},
    "opacity":{"value":0.3}, "size":{"value":3}, "line_linked":{"enable":true,"distance":150,"color":"#fff","opacity":0.2,"width":1},
    "move":{"enable":true,"speed":1}
  },
  "interactivity": { "detect_on":"canvas", "events":{"onhover":{"enable":true,"mode":"grab"}} }
});
</script>
""", unsafe_allow_html=True)

# -----------------------
# Dark Mode
# -----------------------
dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
bg_color = "#121212" if dark_mode else "#FFF"
text_color = "#FFF" if dark_mode else "#000"

st.markdown(f"""
<style>
    body {{ background-color:{bg_color}; color:{text_color}; }}
    button:hover {{ transform:scale(1.05); transition:0.3s; }}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Section Anchors
# -----------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

# -----------------------

# -----------------------
def animated_intro():
    text = "Hi, I'm Samuel Ekisa | I design | I build | I innovate"
    placeholder = st.empty()
    displayed = ""
    
    for char in text:
        displayed += char
        placeholder.markdown(
            f'''
            <h1 style="
                text-align:center;
                color: #ffffff;               /* Fill color while typing */
                -webkit-text-stroke: 1.5px #000000; /* Black outline */
                font-weight:700;
                font-size:2.5rem;
                margin-top:50px;
                margin-bottom:50px;
            ">
                {displayed}
            </h1>
            ''',
            unsafe_allow_html=True
        )
        time.sleep(0.05)

# -----------------------
# Call Hero
# -----------------------
animated_intro()


# -----------------------
# Skills Section (Interactive, Professional)
# -----------------------
st.header("Skills.")

# Load skills from JSON
if SKILLS_FILE.exists():
    with open(SKILLS_FILE) as f:
        skills = json.load(f)
else:
    skills = [
        {"name": "Python", "level": 95, "description": "Automation, AI, backend systems.", "icon": "🐍"},
        {"name": "JavaScript", "level": 75, "description": "Frontend interactivity, web apps.", "icon": "🟨"},
        {"name": "Streamlit", "level": 85, "description": "Interactive dashboards and apps.", "icon": "💻"},
        {"name": "Data Analysis", "level": 90, "description": "Pandas, NumPy, visualization.", "icon": "📊"},
        {"name": "Problem Solving", "level": 100, "description": "Algorithms and critical thinking.", "icon": "🧠"},
        {"name": "UI/UX Design", "level": 70, "description": "User-friendly interfaces.", "icon": "🎨"}
    ]

cols = st.columns(3)

for i, skill in enumerate(skills):
    with cols[i % 3]:
        # Skill header with icon and name
        st.markdown(f"### {skill['icon']} {skill['name']}")
        # Progress bar representing skill level
        st.progress(skill['level'])
        # Expandable description
        with st.expander("Learn more"):
            st.write(skill['description'])



# MY WORK SECTION
# -----------------------
import streamlit as st

st.markdown("---")
st.header("My Work 💼")
st.write("I build systems that **automate**, **educate**, and **inspire** innovation.")


# --- Styling ---
st.markdown("""
<style>
.project-card {
    background-color: #ffffff;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
    padding: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}
.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
}
.project-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #111;
}
.project-desc {
    color: #555;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}
.tech-stack {
    font-size: 0.85rem;
    color: #888;
    margin-top: 0.5rem;
}
.project-link a {
    text-decoration: none;
    color: #0078ff;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --- Work Showcase ---
projects = [
    {
        "title": "Automation System Dashboard",
        "desc": "A real-time Streamlit dashboard that automates workflows and reports for small businesses.",
        "tech": "Python, Streamlit, Supabase, REST APIs",
        "link": "https://github.com/Kidotih/dynamic-knowledge-dashboard"
    },
    {
        "title": "Learning Hub Platform",
        "desc": "A digital platform that simplifies learning through structured modules and AI-based feedback.",
        "tech": "React, FastAPI, PostgreSQL, OpenAI API",
        "link": "https://github.com/Kidotih/learning-hub"
    },
    {
        "title": "Portfolio & Blog System",
        "desc": "A personal web system to document my projects, insights, and progress as a builder and educator.",
        "tech": "Python, Streamlit, Markdown, GitHub Actions",
        "link": "https://github.com/Kidotih/samuel_ekisa_portfolio"
    }
]

cols = st.columns(3)
for col, project in zip(cols, projects):
    with col:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['title']}</div>
            <div class="project-desc">{project['desc']}</div>
            <div class="tech-stack">🧠 {project['tech']}</div>
            <div class="project-link" style="margin-top:10px;">
                🔗 <a href="{project['link']}" target="_blank">View Project</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Closing message
st.markdown("""
<div style="text-align:center; margin-top:3rem; font-size:1.1rem; color:#444;">
✨ I build systems that <b>automate</b>, <b>educate</b>, and <b>inspire.</b>
</div>
""", unsafe_allow_html=True)

# Interactive Mini-Demos Section (instead of games)
# -----------------------
st.header("Interactive Demos.")

demo_cols = st.columns(3, gap="large")

with demo_cols[0]:
    st.subheader("Instant Idea Generator")
    user_input = st.text_input("Type your name or a word")
    if st.button("Generate Idea"):
        st.success(f"💡 Here's an idea for you, {user_input}: Build a smart automation to save time!")

with demo_cols[1]:
    st.subheader("Visual Automation Demo")
    if st.button("Show Demo"):
        st.image("https://media.giphy.com/media/xT0GqssRweIhlz209i/giphy.gif", use_column_width=True)
        st.info("This shows a workflow automation in action!")

with demo_cols[2]:
    st.subheader("Quick Fun Quiz")
    st.write("What's more important for productivity?")
    option = st.radio("", ["Automation", "Learning", "Creativity"])
    if st.button("Submit Answer"):
        st.success(f"You chose: {option}. Great choice!")

st.markdown("---")

# -----------------------
# Timeline Section
# -----------------------
st.header("Timeline & Experience.")
render_timeline(EXPERIENCE_FILE)
st.markdown("---")

# -----------------------
# Analytics Section


# -----------------------


import streamlit as st
import time

st.markdown("---")
st.header("Stats & Achievements.")
st.markdown("<br>", unsafe_allow_html=True)

# Define stats
stats = [
    {"label": "Projects Completed", "value": 12, "icon": "📁"},
    {"label": "Languages Known", "value": 5, "icon": "📝"},
    {"label": "GitHub Commits", "value": 20, "icon": "💻"},
]

# Create columns dynamically
cols = st.columns(len(stats), gap="medium")

# Store placeholders and static info
placeholders = []

for col, stat in zip(cols, stats):
    with col:
        placeholder = st.empty()  # Empty placeholder for number
        placeholders.append((placeholder, stat["value"], stat["icon"], stat["label"]))

        # Initial card with 0
        placeholder.markdown(f"""
        <div style="
            background-color: #ffffff;
            color: #000;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        ">
            <div style="font-size:2rem">{stat['icon']}</div>
            <div style="font-size:1.8rem; font-weight:700; margin-top:10px;">0</div>
            <div style="font-size:0.95rem; color:#555; margin-top:5px;">{stat['label']}</div>
        </div>
        """, unsafe_allow_html=True)

# Animate numbers inside the same cards
for placeholder, target_value, icon, label in placeholders:
    for i in range(target_value + 1):
        placeholder.markdown(f"""
        <div style="
            background-color: #ffffff;
            color: #000;
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        ">
            <div style="font-size:2rem">{icon}</div>
            <div style="font-size:1.8rem; font-weight:700; margin-top:10px;">{i}</div>
            <div style="font-size:0.95rem; color:#555; margin-top:5px;">{label}</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.05)



# -----------------------
# CONTACT SECTION
# -----------------------
import requests
import streamlit as st

st.markdown("---")
st.header("Let's Connect 🤝")
st.write("Ask me about my work, services, or collaborations!")

# --- Styling ---
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #ffffff;
    color: #000;
    border-radius: 10px;
    font-weight: 600;
    padding: 0.6rem 2rem;
    border: none;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    transition: all 0.3s ease-in-out;
}
div.stButton > button:first-child:hover {
    background-color: #f0f0f0;
    transform: translateY(-3px);
}
textarea, input {
    border-radius: 8px !important;
}
.contact-footer {
    text-align: center;
    color: #ccc;
    margin-top: 2rem;
    font-size: 0.9rem;
}
.contact-footer a {
    color: #fff;
    text-decoration: none;
    margin: 0 0.5rem;
    transition: color 0.3s ease;
}
.contact-footer a:hover {
    color: #00aced;
}
</style>
""", unsafe_allow_html=True)

# --- Formspree Endpoint ---
FORM_ENDPOINT = "https://formspree.io/f/meopbnnk"

# --- Contact Form ---
with st.form("contact_form_v3", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", placeholder="Type your message here...")

    submitted = st.form_submit_button("Send Message")

    if submitted:
        if not name or not email or not message:
            st.warning("⚠️ Please fill in all fields before submitting.")
        elif "@" not in email:
            st.error("❌ Please enter a valid email address.")
        else:
            data = {"name": name, "email": email, "message": message}
            try:
                response = requests.post(FORM_ENDPOINT, data=data)
                if response.status_code == 200:
                    st.success(f"✅ Thank you {name}! Your message was sent successfully.")
                    st.balloons()
                else:
                    st.error("⚠️ Something went wrong. Please try again later.")
            except Exception:
                st.error("⚠️ Could not send your message. Please check your connection.")

# --- Contact Footer ---
st.markdown("""
<div class="contact-footer">
    <p>📧 <b>Email:</b> <a href="mailto:samuelekisa@gmail.com">samuelekisa@gmail.com</a></p>
    <p>
        🌐 <a href="https://www.linkedin.com/in/samuelekisa" target="_blank">LinkedIn</a> |
        🐙 <a href="https://github.com/Kidotih" target="_blank">GitHub</a> |
        💼 <a href="https://twitter.com/samuelekisa" target="_blank">Twitter</a>
    </p>
    <p>⚙️ Built by <b>samuel</b></p>
</div>
""", unsafe_allow_html=True)

# Footer end
# -----------------------

