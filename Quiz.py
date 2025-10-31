import streamlit as st 
st.write("Welcome to Quiz game ")
st.write("how are you ")
st.write("steal a brainrot")
Set page title
st.set_page_config(page_title="Quiz Game", page_icon="🎯", layout="centered")

st.title("🎯 Python Quiz Game")
st.write("Answer 5 questions. You’ll get **+1** for every correct answer — no negative marks!")

# Questions data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which of the following is a mammal?",
        "options": ["Crocodile", "Shark", "Whale", "Penguin"],
        "answer": "Whale"
    },
    {
        "question": "What is 15 + 6?",
        "options": ["21", "20", "22", "19"],
        "answer": "21"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Earth", "Mars", "Jupiter"],
        "answer": "Mars"
    }
]

# Store answers
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False
  
