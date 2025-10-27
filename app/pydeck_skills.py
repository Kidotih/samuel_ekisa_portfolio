import pydeck as pdk
import pandas as pd
import streamlit as st
import json
from pathlib import Path

# Resolve path relative to THIS file
BASE_DIR = Path(__file__).resolve().parent.parent  # points to samuel_ekisa_portfolio/
SKILLS_FILE = BASE_DIR / "data" / "skills.json"

def load_skills():
    if not SKILLS_FILE.exists():
        st.error(f"Skills file not found at: {SKILLS_FILE}")
        return pd.DataFrame()  # return empty DataFrame to avoid crash
    with SKILLS_FILE.open() as f:
        return pd.DataFrame(json.load(f))

def render_skill_map():
    skills = load_skills()
    if skills.empty:
        st.info("No skills data to display.")
        return

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
    view_state = pdk.ViewState(latitude=20, longitude=20, zoom=1, pitch=45)
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{Skill}: {Proficiency}%"}
    )
    st.pydeck_chart(deck)
