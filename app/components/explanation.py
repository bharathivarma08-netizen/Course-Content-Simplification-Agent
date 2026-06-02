import streamlit as st
from components.pdf_upload import show_pdf_upload
from components.references import show_references
from core.simplifier import (
    generate_explanation,
    generate_doubt_response
)

from core.memory import (
    save_topic,
    get_context_summary,
    add_to_history
)

from components.key_points import show_key_points
from components.revision import show_revision
from components.important_questions import show_important_questions
from components.voice_input import get_voice_input
from components.pdf_export import show_pdf_download
from components.history import show_history
def show_explanation():

    st.title("🎓 EduBot")

    level = st.session_state.get(
        "student_level",
        "BTech"
    )

    style = st.session_state.get(
        "learning_style",
        "Step-by-step learner"
    )

    st.markdown(
        f"`Level: {level}` &nbsp;&nbsp;&nbsp; "
        f"`Style: {style}`"
    )

    st.markdown("---")
    get_voice_input()


    # ====================================
    # TOPIC INPUT
    # ====================================
    topic = st.text_input(
        "What topic do you want to learn?",
        placeholder=(
            "e.g. Operating System, "
            "Photosynthesis, DBMS Normalization"
        )
    )


    # ====================================
    # GENERATE EXPLANATION
    # ====================================
    if st.button(
        "📘 Explain This Topic",
        use_container_width=True
    ):

        if not topic.strip():

            st.warning(
                "Please enter a topic first."
            )

            return


        save_topic(topic)

        add_to_history(
            "user",
            f"Explain: {topic}"
        )


        with st.spinner(
            "EduBot is preparing your explanation..."
        ):

            explanation = generate_explanation(
                topic,
                level,
                style
            )


        add_to_history(
            "assistant",
            explanation
        )

        st.session_state.last_explanation = explanation

        st.session_state.last_topic = topic


    # ====================================
    # SHOW EXPLANATION
    # ====================================
    if "last_explanation" in st.session_state:

        st.markdown("---")

        st.markdown(
            st.session_state.last_explanation
        )
        show_references(
    st.session_state.last_topic
        )

        st.markdown("---")


        # ====================================
        # LEARNING TOOLS
        # ====================================
        st.markdown(
            "## 📚 What would you like to do next?"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                "❓ Ask a Doubt",
                use_container_width=True
            ):

                st.session_state.show_doubt = True


        with col2:

            if st.button(
                "🧠 Take MCQ Quiz",
                use_container_width=True
            ):

                st.session_state.show_quiz = True

                st.rerun()


        with col3:

            if st.button(
                "📌 Key Points",
                use_container_width=True
            ):

                st.session_state.show_keypoints = (
                    not st.session_state.get(
                        "show_keypoints",
                        False
                    )
                )


        st.markdown("---")


        # ====================================
        # DOUBT SECTION
        # ====================================
        # ====================================
        # DOUBT SECTION
        # ====================================
        if st.session_state.get("show_doubt"):

            st.markdown("## ❓ Ask Your Doubt")

            doubt = st.text_input(
                "Type your doubt here...",
                placeholder=(
                    "Ask anything you didn't understand"
                )
            )

            if st.button(
                "Submit Doubt",
                use_container_width=True
            ):

                if doubt.strip():

                    context = get_context_summary()

                    add_to_history(
                        "user",
                        doubt
                    )

                    with st.spinner(
                        "EduBot is simplifying the answer..."
                    ):

                        doubt_response = generate_doubt_response(
                            doubt=doubt,
                            topic=st.session_state.get(
                                "last_topic",
                                ""
                            ),
                            level=level,
                            style=style,
                            context=context
                        )

                    add_to_history(
                        "assistant",
                        doubt_response
                    )

                    st.success(
                        "Doubt Solved!"
                    )

                    st.markdown(
                        doubt_response
                    )

                else:

                    st.warning(
                        "Please type your doubt first."
                    )


        # ====================================
        # KEY POINTS
        # ====================================
        if st.session_state.get("show_keypoints"):

            show_key_points()


        # ====================================
        # QUICK REVISION
        # ====================================
        with st.expander("⚡ Quick Revision"):

            show_revision()


        # ====================================
        # IMPORTANT QUESTIONS
        # ====================================
        with st.expander("📝 Important Questions"):

            show_important_questions()
         # ====================================
        # PDF UPLOAD FEATURE
        # ====================================
        show_pdf_upload()
        show_pdf_download()
    with st.expander("🕘 Learning History"):

        show_history()
