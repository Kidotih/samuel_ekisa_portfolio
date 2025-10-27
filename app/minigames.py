import streamlit as st
import random

def quiz_game():
    st.subheader("Mini Coding Quiz")
    questions = {
        "Python is dynamically typed?": "Yes",
        "Is 2+2 equal 5?": "No",
        "Git is a version control system?": "Yes"
    }
    q, a = random.choice(list(questions.items()))
    answer = st.text_input(q)
    if answer:
        if answer.lower() == a.lower():
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect, try again!")

def puzzle_game():
    st.subheader("Guess the Number")
    number = random.randint(1, 20)
    guess = st.number_input("Enter a number between 1-20", min_value=1, max_value=20, step=1)
    if st.button("Check"):
        if guess == number:
            st.success("🎉 Correct! You found the number.")
        else:
            st.warning(f"Try again! The number was {number}.")
