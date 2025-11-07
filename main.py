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






import streamlit as st

st.markdown("---")
st.header(" Timeline & Experience🧭")
st.caption("Select a company to reveal full experience details on the right. Scroll-free, interactive, professional design.")

# --- Timeline Data ---

# Example of updated skill_notes
timeline_data = [
    {
        "company": "Innovate Systems Ltd.",
        "role": "Software Developer",
        "date": "Jan 2023 – Present",
        "desc": [
            "Architecting and deploying intelligent automation systems with Python and Streamlit.",
            "Building scalable APIs and dashboards for data-driven decision-making.",
            "Collaborating cross-functionally to deliver high-impact digital solutions."
        ],
        "skill_note": "🚀 Automating workflows & building intelligent APIs with Python & Streamlit"
    },
    {
        "company": "NextGen Technologies",
        "role": "AI & Automation Intern",
        "date": "Jun 2022 – Dec 2022",
        "desc": [
            "Developed prototypes integrating AI models into real-world workflows.",
            "Enhanced automation pipelines using TensorFlow, Pandas, and FastAPI.",
            "Improved system reliability and efficiency by 30% through optimized code design."
        ],
        "skill_note": "🤖 Prototyping AI-driven automation that boosts efficiency"
    },
    {
        "company": "Tech Innovators Hub",
        "role": "Junior Developer",
        "date": "Jan 2022 – May 2022",
        "desc": [
            "Assisted in backend development and database management using PostgreSQL.",
            "Gained experience in DevOps, version control, and UI/UX design principles.",
            "Contributed to early product testing and feature prototyping."
        ],
        "skill_note": "💡 Building foundations in backend dev, DevOps & UI/UX"
    }
]

# --- CSS for premium timeline design ---
st.markdown("""
<style>
/* Timeline container */
.timeline-wrapper {
    display: flex;
    max-width: 900px;
    margin: 40px auto;
    font-family: sans-serif;
}

/* Left column: timeline line and companies */
.timeline-left {
    flex: 1;
    position: relative;
    padding-right: 20px;
}
.timeline-left::before {
    content: '';
    position: absolute;
    left: 20px;
    top: 0;
    bottom: 0;
    width: 4px;
    background: linear-gradient(180deg, #007bff, #6f42c1);
    border-radius: 2px;
}

/* Dot for each company */
.timeline-left p {
    position: relative;
    margin: 40px 0;
    padding-left: 15px;
    cursor: pointer;
    font-weight: 600;
    color: #007bff;
}
.timeline-left p::before {
    content: '';
    position: absolute;
    left: -7px;
    top: 3px;
    width: 14px;
    height: 14px;
    background: #fff;
    border: 3px solid #007bff;
    border-radius: 50%;
    box-shadow: 0 0 10px rgba(0,123,255,0.3);
}

/* Right column: details card */
.timeline-right {
    flex: 2;
    padding-left: 30px;
    min-height: 300px;
    position: relative;
}
.timeline-card {
    background: linear-gradient(145deg, #ffffff, #f0f0f8);
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    padding: 20px;
    transition: all 0.3s ease;
}
.timeline-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}
.timeline-card h3 {
    margin: 0 0 5px 0;
    color: #007bff;
    font-size: 1.1rem;
}
.timeline-card h4 {
    margin: 0 0 10px 0;
    font-size: 0.95rem;
    color: #333;
}
.timeline-card p {
    font-size: 0.85rem;
    color: #555;
    margin-bottom: 8px;
}
.timeline-card ul {
    padding-left: 18px;
    margin: 5px 0 0 0;
}
.timeline-card ul li {
    margin-bottom: 5px;
    font-size: 0.82rem;
    color: #444;
}

/* Mobile responsive */
@media screen and (max-width: 768px) {
    .timeline-wrapper {
        flex-direction: column;
    }
    .timeline-left::before {
        left: 10px;
    }
    .timeline-left p::before {
        left: -5px;
    }
    .timeline-right {
        padding-left: 15px;
        margin-top: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Layout: two columns ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("**Companies & Key Skills:**")
    selected_company = st.radio(
        "Select a company to reveal details",
        [item["company"] for item in timeline_data],
        index=0
    )
    for item in timeline_data:
        st.markdown(f"* {item['skill_note']}")

with col2:
    selected = next(item for item in timeline_data if item["company"] == selected_company)
    st.markdown(f"""
    <div class="timeline-card">
        <h3>{selected['role']}</h3>
        <h4>{selected['company']}</h4>
        <p><em>{selected['date']}</em></p>
        <ul>
            {"".join([f"<li>{point}</li>" for point in selected['desc']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)


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

