import streamlit as st
from components import animated_intro, cta_buttons
from minigames import quiz_game, puzzle_game
from timeline import render_timeline
from analytics import render_analytics
from chatbot import chatbot
import json
from pathlib import Path
import time

import streamlit as st

st.set_page_config(page_title="Samuel Ekisa | Portfolio", layout="wide")

# -----------------------------
# FIXED WHITE NAVBAR
# -----------------------------
st.markdown("""
<style>
/* Reset default padding */
[data-testid="stAppViewContainer"] > .main {
    padding-top: 0rem;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
section[data-testid="stSidebar"] {
    background-color: #fff;
}

/* Navbar container */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(10px);
  display: flex;
  justify-content: center;
  gap: 40px;
  padding: 14px 0;
  border-bottom: 1px solid #e0e0e0;
  z-index: 9999;
}

/* Navbar links */
.navbar a {
  color: #111;
  text-decoration: none;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  transition: color 0.3s ease, transform 0.3s ease;
}
.navbar a:hover {
  color: #007bff;
  transform: translateY(-2px);
}

/* Add smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>

<div class="navbar">
  <a href="#home">Home</a>
  <a href="#skills">Skills</a>
  <a href="#projects">Projects</a>
  <a href="#timeline">Timeline</a>
  <a href="#contact">Contact</a>
</div>
st.markdown("""
<script>
document.querySelectorAll('.navbar a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      window.scrollTo({
        top: target.offsetTop - 70,
        behavior: 'smooth'
      });
    }
  });
});
</script>
""", unsafe_allow_html=True)

""", unsafe_allow_html=True)

# Prevent content from being hidden under navbar
st.markdown("<div style='margin-top:80px;'></div>", unsafe_allow_html=True)



# -----------------------
# Page Configuration
# -----------------------


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
# SKILLS SECTION — WHITE THEME + ANIMATED + TOOLTIP + SEO OPTIMIZED
# -----------------------
import streamlit as st
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)


st.markdown("---")
st.header("Skills & Expertise ⚙️")
st.caption("Empowering ideas through automation, data, and intelligent design — with clean, modern engineering.")

# --- Styling ---
st.markdown("""
<style>
@keyframes fadeInUp {
  from {opacity: 0; transform: translateY(20px);}
  to {opacity: 1; transform: translateY(0);}
}
.category {
    margin-bottom: 2rem;
    animation: fadeInUp 1s ease;
}
.category h3 {
    color: #111;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 0.3rem;
    letter-spacing: 0.5px;
}
.skill-box {
    background: #ffffff;
    border: 1px solid #e6e6e6;
    border-radius: 12px;
    padding: 1rem 1.3rem;
    margin-bottom: 0.9rem;
    transition: all 0.4s ease;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    animation: fadeInUp 1s ease;
}
.skill-box:hover {
    background: #f9f9f9;
    border-color: #ccc;
    transform: translateX(5px);
}
.skill-name {
    font-weight: 700;
    color: #111;
    font-size: 1.05rem;
}
.skill-note {
    color: #444;
    font-size: 0.9rem;
    margin-top: 0.3rem;
}
.progress {
    background-color: #eaeaea;
    border-radius: 10px;
    overflow: hidden;
    height: 8px;
    margin-top: 0.5rem;
}
.progress-bar {
    height: 8px;
    border-radius: 10px;
    background: linear-gradient(90deg, #007bff, #00bfff);
    transition: width 1s ease;
}
.skill-tooltip {
    display: inline-block;
    position: relative;
    cursor: help;
}
.skill-tooltip .tooltip-text {
    visibility: hidden;
    width: 230px;
    background: #111;
    color: #fff;
    text-align: left;
    border-radius: 6px;
    padding: 8px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -115px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.8rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}
.skill-tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)

# --- Skills Data ---
categories = {
    "⚙️ Programming & Development": [
        {
            "icon": "🐍",
            "name": "Python",
            "note": "Advanced Python for backend automation, AI integration, and scalable API systems using FastAPI, Flask, and Streamlit.",
            "tooltip": "Expert in automation pipelines, backend design, and AI-driven Python development.",
            "level": 95
        },
        {
            "icon": "🟨",
            "name": "JavaScript",
            "note": "Modern JavaScript (ES6+) for dynamic web apps, frontend logic, and real-time interfaces.",
            "tooltip": "Building interactive, API-powered experiences with asynchronous logic and clean UI structure.",
            "level": 85
        },
        {
            "icon": "💻",
            "name": "Streamlit",
            "note": "Building interactive dashboards, automation tools, and machine learning interfaces.",
            "tooltip": "Expert in Streamlit app development for intelligent data-driven visualization.",
            "level": 92
        }
    ],
    "🤖 AI & Data Intelligence": [
        {
            "icon": "🧠",
            "name": "Machine Learning",
            "note": "Building predictive models, feature engineering, and deploying AI solutions using TensorFlow and Scikit-learn.",
            "tooltip": "Proficient in ML model lifecycle — training, evaluation, deployment, and automation.",
            "level": 88
        },
        {
            "icon": "📊",
            "name": "Data Visualization",
            "note": "Transforming data into insights using Matplotlib, Plotly, and custom Streamlit visualizations.",
            "tooltip": "Data storytelling for analytics and strategic decision-making.",
            "level": 90
        },
        {
            "icon": "🧮",
            "name": "Data Engineering",
            "note": "ETL pipelines, real-time data flow, and analytics optimization with SQL, Pandas, and cloud tools.",
            "tooltip": "Designing scalable data pipelines for performance and accuracy.",
            "level": 87
        }
    ],
    "🎨 Frontend & Design Systems": [
        {
            "icon": "⚛️",
            "name": "React (Basics)",
            "note": "Building modular and interactive interfaces using React and component-based logic.",
            "tooltip": "Crafting responsive and dynamic web layouts.",
            "level": 75
        },
        {
            "icon": "🎨",
            "name": "UI/UX Design",
            "note": "Designing human-centered, accessible, and visually consistent experiences.",
            "tooltip": "Focus on clean aesthetics and modern design language.",
            "level": 85
        },
        {
            "icon": "🌐",
            "name": "Web Fundamentals",
            "note": "Responsive layouts using HTML5, CSS3, and SEO-optimized content structure.",
            "tooltip": "Ensuring pixel-perfect, high-performance frontend delivery.",
            "level": 88
        }
    ],
    "☁️ Cloud, DevOps & Automation": [
        {
            "icon": "🔗",
            "name": "Supabase / Firebase",
            "note": "Integrating real-time databases, authentication, and cloud services for modern apps.",
            "tooltip": "Building connected, secure, and scalable backend ecosystems.",
            "level": 82
        },
        {
            "icon": "🐳",
            "name": "Docker",
            "note": "Containerizing applications for deployment, scalability, and collaboration.",
            "tooltip": "Efficient environment management for full-stack projects.",
            "level": 80
        },
        {
            "icon": "🧩",
            "name": "Git & CI/CD",
            "note": "Version control, workflow automation, and continuous deployment using GitHub Actions.",
            "tooltip": "Streamlining collaboration and delivery pipelines.",
            "level": 93
        }
    ]
}

# --- Display Layout ---
cols = st.columns(2)
cat_names = list(categories.keys())

for i, col in enumerate(cols):
    with col:
        for cat in cat_names[i::2]:
            st.markdown(f"<div class='category'><h3>{cat}</h3>", unsafe_allow_html=True)
            for skill in categories[cat]:
                progress_html = f"""
                <div class="progress"><div class="progress-bar" style="width:{skill['level']}%"></div></div>
                """
                tooltip_html = f"""
                <div class="skill-tooltip">
                    <div class="skill-name">{skill['icon']} {skill['name']}</div>
                    <div class="tooltip-text">{skill['tooltip']}</div>
                </div>
                """
                st.markdown(f"""
                <div class="skill-box">
                    {tooltip_html}
                    <div class="skill-note">{skill['note']}</div>
                    {progress_html}
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


# MY WORK SECTION
# -----------------------
import streamlit as st

st.markdown("---")
st.markdown('<div id="work"></div>', unsafe_allow_html=True)
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
st.markdown('<div id="timeline"></div>', unsafe_allow_html=True)
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

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
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

