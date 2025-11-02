# components.py
import streamlit as st
import time

def animated_intro():
    text = "Hi, I'm Samuel Ekisa | I design | I build | I innovate"
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(
            f'<h2 style="text-align:center; margin-top:50px;">{displayed}</h2>',
            unsafe_allow_html=True
        )
        time.sleep(0.05)

def cta_buttons():
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button(" My Work"):
            st.session_state["section"] = "projects"
            st.experimental_rerun()
    with col2:
        if st.button("Let's Connect"):
            st.session_state["section"] = "contact"
            st.experimental_rerun()

# -----------------------
# Interactive Skill Cloud
# -----------------------
def skill_cloud():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("## 🧠 My Skills", unsafe_allow_html=True)
    st.caption("Tap a skill to see what I do with it.")

    skills = [
        "Python", "Streamlit", "Automation", "Supabase",
        "UI Design", "APIs", "Data Visualization", "AI & Chatbots"
    ]

    cols = st.columns(4, gap="large")
    for i, skill in enumerate(skills):
        with cols[i % 4]:
            if st.button(f"💡 {skill}", key=skill):
                st.success(f"**{skill}** — I apply it to build smart, user-focused systems.")
                st.info(skill_details(skill))

def skill_details(skill):
    details = {
        "Python": "I use it for backend logic, data automation, and intelligent systems.",
        "Streamlit": "For rapid prototyping and deploying data apps easily.",
        "Automation": "I build scripts and tools that save time and remove repetitive work.",
        "Supabase": "Used as my go-to backend for authentication and real-time data.",
        "UI Design": "I create minimal, responsive, and user-friendly interfaces.",
        "APIs": "I integrate and design APIs for scalable automation.",
        "Data Visualization": "Turning raw data into insight with Streamlit and PyDeck.",
        "AI & Chatbots": "Experimenting with conversational systems that learn and adapt."
    }
    return details.get(skill, "I’m always improving my workflow around this skill.")


