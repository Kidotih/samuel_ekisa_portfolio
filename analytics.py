import streamlit as st

def render_analytics():
    st.subheader("Stats & Achievements")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Projects Completed", 12)
    with col2:
        st.metric("Languages Known", 5)
    with col3:
        st.metric("GitHub Commits", 250)
