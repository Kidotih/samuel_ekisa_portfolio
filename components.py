import streamlit as st
import time

# -----------------------
# Animated Typing Intro
# -----------------------
def animated_intro():
    text = "Hi, I'm Samuel Ekisa | I design | I build | I innovate"
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(f'<h2 style="text-align:center; margin-top:50px;">{displayed}</h2>', unsafe_allow_html=True)
        time.sleep(0.05)

# -----------------------
# CTA Buttons (functional)
# -----------------------
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
