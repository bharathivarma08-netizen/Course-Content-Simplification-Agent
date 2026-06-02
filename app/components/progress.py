import streamlit as st


# =====================================
# UPDATE QUIZ PROGRESS
# =====================================
def update_progress(score, total):

    if "quiz_history" not in st.session_state:

        st.session_state.quiz_history = []

    st.session_state.quiz_history.append({

        "score": score,

        "total": total
    })


# =====================================
# SHOW LEARNING PROGRESS
# =====================================
def show_progress():

    st.markdown("## 📈 Learning Progress")

    history = st.session_state.get(
        "quiz_history",
        []
    )

    if not history:

        st.info(
            "No quiz attempts yet."
        )

        return

    total_quizzes = len(history)

    total_score = sum(
        item["score"]
        for item in history
    )

    total_questions = sum(
        item["total"]
        for item in history
    )

    percentage = int(
        (total_score / total_questions) * 100
    )

    st.metric(
        "Quiz Accuracy",
        f"{percentage}%"
    )

    st.progress(
        percentage / 100
    )

    st.markdown("---")

    st.markdown(
        f"✅ Quizzes Attempted: {total_quizzes}"
    )

    st.markdown(
        f"✅ Questions Solved: {total_questions}"
    )

    st.markdown(
        f"✅ Correct Answers: {total_score}"
    )