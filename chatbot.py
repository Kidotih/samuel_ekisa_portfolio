import streamlit as st

def chatbot():
    st.subheader("Ask me about my work!")
    question = st.text_input("Type your question here:")
    if question:
        if "project" in question.lower():
            st.info("I have several projects including a portfolio website and mini-games app.")
        elif "skills" in question.lower():
            st.info("I specialize in Python, AI, Web Development, and Data Structures.")
        else:
            st.info("I’m happy to answer more about my experience or projects!")

