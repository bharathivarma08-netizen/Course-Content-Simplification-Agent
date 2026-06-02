import streamlit as st
from core.granite_client import ask_granite


def generate_key_points(topic, level):

    prompt = f"""
Generate 10 important key points for:
{topic}

Student Level:
{level}

Rules:
- Use simple language
- Keep points short
- Focus on important exam concepts
- Use bullet points
- Easy to remember
"""

    response = ask_granite(prompt)

    return response


def show_key_points():

    st.markdown("---")
    st.markdown("## 📌 Points to Remember")

    topic = st.session_state.get("last_topic", "")
    level = st.session_state.get("student_level", "BTech")

    if not topic:
        st.warning("Please learn a topic first.")
        return

    if st.button("Generate Key Points", use_container_width=True):

        with st.spinner("Generating key points..."):

            key_points = generate_key_points(topic, level)

            st.success("Important Points Ready!")

            st.markdown(key_points)

