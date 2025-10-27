import pydeck as pdk
import pandas as pd
import streamlit as st
import json
import os

# ------------------------
# Path to skills.json
# ------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_FILE = os.path.join(BASE_DIR, "data", "skills.json")

# ------------------------
# Load skills into DataFrame
# ------------------------
def load_skills():
    with open(SKILLS_FILE) as f:
        return pd.DataFrame(json.load(f))

# ------------------------
# Render 3D Skill Map
# ------------------------
def render_skill_map():
    skills = load_skills()

    layer = pdk.Layer(
        "ColumnLayer",
        data=skills,
        get_position="[lon, lat]",
        get_elevation="Proficiency * 1000",
        radius=100000,
        get_fill_color="[255 - Proficiency*2, Proficiency*2, 150]",
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=20,
        longitude=20,
        zoom=1,
        pitch=45
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{Skill}: {Proficiency}%"}
    )

    st.pydeck_chart(r)
