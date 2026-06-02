import streamlit as st
from core.granite_client import ask_granite


def generate_important_questions(topic, level):

    prompt = f"""
Generate important exam questions for:
{topic}

Student Level:
{level}

Rules:
- Generate:
    - 5 short-answer questions
    - 5 long-answer questions
- Use exam-oriented style
- Keep questions clear and educational
"""

    response = ask_granite(prompt)

    return response


def show_important_questions():

    st.markdown("---")
    st.markdown("## 📝 Important Questions")

    topic = st.session_state.get("last_topic", "")
    level = st.session_state.get("student_level", "BTech")

    if not topic:
        st.warning("Please learn a topic first.")
        return

    if st.button("Generate Important Questions", use_container_width=True):

        with st.spinner("Generating important questions..."):

            questions = generate_important_questions(topic, level)

            st.success("Important Questions Ready!")

            st.markdown(questions)

