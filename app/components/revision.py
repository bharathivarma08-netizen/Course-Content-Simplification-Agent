import streamlit as st
from core.granite_client import ask_granite


def generate_revision(topic, level):

    prompt = f"""
You are an educational revision assistant.

Create a QUICK REVISION for the topic:
{topic}

Student Level:
{level}

Rules:
- Use very simple language
- Maximum 10 bullet points
- Focus on exam revision
- Keep each point short
- Highlight important concepts only
"""

    response = ask_granite(prompt)

    return response


def show_revision():

    st.markdown("---")
    st.markdown("## ⚡ Quick Revision")

    topic = st.session_state.get("last_topic", "")
    level = st.session_state.get("student_level", "BTech")

    if not topic:
        st.warning("Please learn a topic first.")
        return

    if st.button("Generate Quick Revision", use_container_width=True):

        with st.spinner("Generating revision notes..."):

            revision = generate_revision(topic, level)

            st.success("Quick Revision Ready!")

            st.markdown(revision)

