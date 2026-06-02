import streamlit as st


# =====================================
# INITIALIZE SESSION MEMORY
# =====================================
def init_memory():

    defaults = {

        "history": [],

        "quiz_history": [],

        "student_level": "BTech",

        "learning_style": "Step-by-step learner",

        "onboarding_done": False
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# =====================================
# SAVE STUDENT LEVEL
# =====================================
def save_level(level):

    st.session_state.student_level = level


# =====================================
# SAVE LEARNING STYLE
# =====================================
def save_style(style):

    st.session_state.learning_style = style


# =====================================
# SAVE CURRENT TOPIC
# =====================================
def save_topic(topic):

    st.session_state.current_topic = topic


# =====================================
# ADD CHAT HISTORY
# =====================================
def add_to_history(role, content):

    if "history" not in st.session_state:

        st.session_state.history = []

    st.session_state.history.append({

        "role": role,

        "content": content
    })


# =====================================
# CONTEXT SUMMARY
# =====================================
def get_context_summary():

    history = st.session_state.get(
        "history",
        []
    )

    summary = ""

    for item in history[-5:]:

        role = item["role"]

        content = item["content"]

        summary += f"{role}: {content}\n"

    return summary