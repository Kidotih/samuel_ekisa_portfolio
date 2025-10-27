import streamlit as st
from components import animated_intro, cta_buttons
from pydeck_skills import render_skill_map
from minigames import quiz_game, puzzle_game
from timeline import render_timeline
from analytics import render_analytics
from chatbot import chatbot
import json
from pathlib import Path

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
    button:hover {{ transform:scale(1.1); transition:0.3s; }}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Section Anchors
# -----------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

# -----------------------
# Hero Section
# -----------------------
animated_intro()
cta_buttons()  # Smooth scroll buttons

st.markdown("---")

# -----------------------
# Skills Section
# -----------------------
st.header("Skills")
render_skill_map()

# -----------------------
# Projects / Work Section
# -----------------------
st.markdown("---")
st.markdown('<div id="projects" style="padding-top:60px;"></div>', unsafe_allow_html=True)
st.header("My Work")

if PROJECTS_FILE.exists():
    with open(PROJECTS_FILE) as f:
        projects = json.load(f)
else:
    projects = []

for project in projects:
    screenshot_path = (BASE_DIR / project["screenshot"]).resolve()
    if not screenshot_path.exists():
        st.warning(f"Screenshot not found: {screenshot_path}")
        continue
    with st.expander(project["name"]):
        st.image(str(screenshot_path), width=300)
        st.write(project["description"])
        st.write("Technologies:", ", ".join(project["tech"]))
        st.markdown(f"[GitHub Repo]({project['github']})")

# -----------------------
# Mini-Games Section
# -----------------------
st.markdown("---")
st.header("Mini-Games")
quiz_game()
puzzle_game()

# -----------------------
# Timeline Section
# -----------------------
st.markdown("---")
render_timeline(EXPERIENCE_FILE)

# -----------------------
# Analytics Section
# -----------------------
st.markdown("---")
render_analytics()

# -----------------------
# Contact Section
# -----------------------
st.markdown("---")
st.markdown('<div id="contact" style="padding-top:60px;"></div>', unsafe_allow_html=True)
st.header("Let's Connect")
chatbot()
st.text_input("Your Name")
st.text_input("Your Email")
st.text_area("Message")
st.button("Send Message")
