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
# Display skills in columns with expanders
cols = st.columns(3)
for i, skill in enumerate(skills):
    with cols[i % 3]:
        with st.expander(f"{skill['name']} ({skill['level']})"):
            st.write(skill['description'])
st.markdown("---")



# -----------------------
# My Work Section
# -----------------------

st.markdown("---")
st.header("My Work.")
st.markdown("<br>", unsafe_allow_html=True)

if PROJECTS_FILE.exists():
    with open(PROJECTS_FILE) as f:
        projects = json.load(f)
else:
    projects = []

# Gather categories for filter
categories = ["All"] + sorted({p.get("category","Other") for p in projects})
selected_category = st.selectbox("Filter by category", categories, key="projects_filter")

# CSS for project cards
st.markdown("""
<style>
.project-card {
    background-color: #fff;
    color: #000;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1.5rem;
    transition: transform 0.3s, box-shadow 0.3s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}
.project-title { font-weight:600; font-size:1.2rem; margin-bottom:0.3rem; }
.project-tech { font-size:0.85rem; color:#555; margin-top:0.5rem; }
.project-container { display:flex; flex-wrap:wrap; gap:1rem; }
.project-img { max-width:300px; border-radius:10px; }
</style>
""", unsafe_allow_html=True)

# Display projects in a flexible grid
st.markdown('<div class="project-container">', unsafe_allow_html=True)

for project in projects:
    if selected_category != "All" and project.get("category","Other") != selected_category:
        continue
    
    screenshot = BASE_DIR / project.get("screenshot","")
    img_url = str(screenshot) if screenshot.exists() else "https://via.placeholder.com/300x200?text=No+Image"
    
    st.markdown(f"""
    <div class="project-card">
        <img src="{img_url}" class="project-img">
        <div class="project-title">{project.get('name','Unnamed Project')}</div>
        <div>{project.get('description','No description available.')}</div>
        <div class="project-tech"><b>Tech:</b> {', '.join(project.get('tech',[]))}</div>
        {f"<a href='{project['github']}' target='_blank'>🔗 View on GitHub</a>" if project.get('github') else ""}
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------
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
    {"label": "GitHub Commits", "value": 250, "icon": "💻"},
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
st.header("Let's Connect..")
chatbot()
st.text_input("Your Name", key="contact_name")
st.text_input("Your Email", key="contact_email")
st.text_area("Message", key="contact_message")
st.button("Send Message", key="contact_send")


# ... all previous sections: Skills, My Work, Mini-Games, Timeline, Analytics, Contact

# -----------------------
# Footer
# -----------------------
st.markdown("<br><br>", unsafe_allow_html=True)  # space before footer
st.markdown("""
<div style="
    background-color:#121212;
    color:#fff;
    text-align:center;
    padding:1rem;
    font-size:0.9rem;
    border-top:1px solid rgba(255,255,255,0.1);
">
    Built with ❤️ by <strong>Samuel Ekisa </strong>
</div>
""", unsafe_allow_html=True)

