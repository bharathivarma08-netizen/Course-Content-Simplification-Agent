import streamlit as st
from core.memory import init_memory
from components.onboarding import show_onboarding
from components.explanation import show_explanation
from components.quiz import show_quiz
from styles import load_css
from components.progress import show_progress
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton button {
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}

.stTextInput input {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
# PAGE CONFIG
st.set_page_config(
    page_title="EduBot — Adaptive Learning Companion",
    page_icon="🎓",
    layout="wide"
)
load_css()

# INITIALIZE MEMORY
init_memory()


# ====================================
# ONBOARDING
# ====================================
if not st.session_state.get("onboarding_done"):

    show_onboarding()


# ====================================
# MAIN APPLICATION
# ====================================
else:

    # QUIZ SCREEN
    if st.session_state.get("show_quiz"):

        show_quiz()

        st.markdown("---")

        if st.button(
            "⬅ Back to Learning",
            use_container_width=True
        ):

            st.session_state.show_quiz = False

            st.rerun()


    # MAIN LEARNING SCREEN
    else:

        show_explanation()


    # ====================================
    # SIDEBAR
    # ====================================
    with st.sidebar:

        st.markdown("## 👤 Your Profile")

        st.markdown(
            f"**📘 Level:** "
            f"{st.session_state.get('student_level', '-')}"
        )

        st.markdown(
            f"**🧠 Style:** "
            f"{st.session_state.get('learning_style', '-')}"
        )

        st.markdown(
            f"**📖 Topic:** "
            f"{st.session_state.get('current_topic', '-')}"
        )

        st.markdown("---")

        if st.button(
            "🔄 Change Level / Style",
            use_container_width=True
        ):

            st.session_state.clear()

            st.rerun()
        show_progress()
st.markdown("---")

st.caption(
    "Built using IBM Granite • Watsonx.ai • Streamlit • ChromaDB"
)
