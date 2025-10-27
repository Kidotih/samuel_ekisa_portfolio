import streamlit as st
import time

# ---------------------------------
# Animated Typing Intro
# ---------------------------------
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

# ---------------------------------
# Safe Rerun Function
# ---------------------------------
try:
    from streamlit.runtime.scriptrunner import RerunException, get_script_run_ctx
except ImportError:
    RerunException = None
    get_script_run_ctx = None

def rerun():
    """Safe rerun for all Streamlit versions."""
    if get_script_run_ctx() is not None and RerunException is not None:
        raise RerunException(get_script_run_ctx())

# ---------------------------------
# CTA Buttons (Navigate between sections)
# ---------------------------------
def cta_buttons():
    st.markdown(
        """
        <style>
        div[data-testid="column"] button {
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 6px;
            border: none;
            background-color: #1E90FF;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        div[data-testid="column"] button:hover {
            background-color: #0B5ED7;
            transform: scale(1.05);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("See My Work", use_container_width=True):
            st.session_state["section"] = "projects"
            rerun()
    with col2:
        if st.button("Let's Connect", use_container_width=True):
            st.session_state["section"] = "contact"
            rerun()
