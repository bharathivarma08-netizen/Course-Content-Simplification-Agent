import streamlit as st
from core.memory import save_level, save_style

def show_onboarding():
    st.title("Welcome to EduBot")
    st.subheader("Your Adaptive AI Learning Companion")
    st.markdown("---")

    st.markdown("### Step 1 — What is your current study level?")
    level = st.selectbox(
        "Select your level",
        [
            "6th Class",
            "10th Class",
            "Intermediate",
            "Diploma",
            "BTech",
            "Beginner",
            "Advanced",
        ],
        index=4
    )

    st.markdown("### Step 2 — How do you learn best?")
    style = st.selectbox(
        "Select your learning style",
        [
            "Step-by-step learner",
            "Visual learner",
            "Real-world examples",
            "Exam-focused learner",
            "Quick revision learner",
        ]
    )

    st.markdown("---")

    if st.button("Start Learning", use_container_width=True):
        save_level(level)
        save_style(style)
        st.session_state.onboarding_done = True
        st.rerun()