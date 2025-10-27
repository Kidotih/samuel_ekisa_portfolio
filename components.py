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
        placeholder.markdown(f'<h3 style="text-align:center">{displayed}</h3>', unsafe_allow_html=True)
        time.sleep(0.05)

# -----------------------
# CTA Buttons with Smooth Scroll
# -----------------------
def cta_buttons():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <button onclick="document.getElementById('projects').scrollIntoView({behavior: 'smooth'});">
            View Projects
            </button>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <button onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'});">
            Contact Me
            </button>
        """, unsafe_allow_html=True)
