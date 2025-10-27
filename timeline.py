import streamlit as st
import json

def render_timeline():
    st.subheader("Experience Timeline")
    with open("data/experience.json") as f:
        experiences = json.load(f)
    for exp in experiences:
        st.markdown(f"**{exp['role']}** at {exp['company']} ({exp['years']})")
        st.write(exp['description'])
        st.markdown("---")
