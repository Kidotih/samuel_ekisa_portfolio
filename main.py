import streamlit as st
from components import animated_intro, cta_buttons
from pydeck_skills import render_skill_map
from minigames import quiz_game, puzzle_game
from timeline import render_timeline
from analytics import render_analytics
from chatbot import chatbot
import json
import os
import time

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="Samuel Ekisa Portfolio", layout="wide")

# -----------------------
# Paths to JSON files
# -----------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS_FILE = os.path.join(BASE_DIR, "data", "projects.json")
SKILLS_FILE = os.path.join(BASE_DIR, "data", "skills.json")
EXPERIENCE_FILE = os.path.join(BASE_DIR, "data", "experience.json")

# -----------------------
# Particle Background
# -----------------------
st.markdown("""
<div id="particles-js" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1;"></div>
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": { "value": 60 },
    "color": { "value": "#ffffff" },
    "shape": { "type": "circle" },
    "opacity": { "value": 0.3 },
    "size": { "value": 3 },
    "line_linked": { "enable": true, "distance": 150, "color": "#ffffff", "opacity": 0.2, "width": 1 },
    "move": { "enable": true, "speed": 1 }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": { "onhover": { "enable": true, "mode": "grab" } }
  }
});
</script>
""", unsafe_allow_html=True)

# -----------------------
# Dark Mode Styling
# -----------------------
dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
bg_color = "#121212" if dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if dark_mode else "#000000"

st.markdown(f"""
    <style>
        body {{
            background-color: {bg_color};
            color: {text_color};
        }}
        button:hover {{
            transform: scale(1.1);
            transition: 0.3s;
        }}
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Section Anchors
# -----------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

# -----------------------
# Session State
# -----------------------
if "section" not in st.session_state:
    st.session_state["section"] = "hero"

# -----------------------
# Hero Section
# -----------------------
if st.session_state["section"] == "hero":
    animated_intro()  # Typing animation
    cta_buttons()    # Smooth-scroll buttons

st.markdown("---")

# -----------------------
# Skills Section
# -----------------------
st.header("Skills")
render_skill_map()  # pydeck_skills_
