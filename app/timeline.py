# timeline.py
import streamlit as st
import json
from pathlib import Path

def render_timeline(json_path):
    json_file = Path(json_path)
    if not json_file.exists():
        st.warning(f"Timeline file not found: {json_file}")
        return

    with open(json_file) as f:
        timeline = json.load(f)

    st.subheader("Experience Timeline")
    for item in timeline:
        role = item.get("role", "N/A")
        company = item.get("company", "N/A")
        start = item.get("start", "")
        end = item.get("end", "")
        description = item.get("description", "")

        st.write(f"**{role}** at {company} ({start} - {end})")
        st.write(description)
