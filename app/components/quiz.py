import streamlit as st
import json
from core.granite_client import ask_granite
from components.progress import update_progress

def generate_mcqs(topic: str, level: str) -> list:
    prompt = f"""
Generate exactly 5 multiple choice questions about "{topic}" for a {level} student.

Return ONLY a valid JSON array.

Format:
[
  {{
    "question": "Question text here?",
    "options": [
      "A) option1",
      "B) option2",
      "C) option3",
      "D) option4"
    ],
    "answer": "A) option1",
    "explanation": "Brief explanation why this is correct."
  }}
]
"""

    raw = ask_granite(prompt)

    try:
        start = raw.find("[")
        end = raw.rfind("]") + 1

        cleaned_json = raw[start:end]

        questions = json.loads(cleaned_json)

        return questions

    except Exception as e:
        st.error(f"Error parsing MCQs: {e}")
        return []


def show_quiz():
    st.markdown("---")
    st.markdown("## 🧠 MCQ Quiz")

    topic = st.session_state.get("last_topic", "")
    level = st.session_state.get("student_level", "BTech")

    if not topic:
        st.warning("Please explain a topic first before taking the quiz.")
        return

    # Generate questions only once
    if (
        "mcq_questions" not in st.session_state
        or st.session_state.get("mcq_topic") != topic
    ):

        with st.spinner("Generating quiz questions using IBM Granite..."):

            st.session_state.mcq_questions = generate_mcqs(topic, level)

            st.session_state.mcq_topic = topic

            st.session_state.mcq_answers = {}

    questions = st.session_state.get("mcq_questions", [])

    if not questions:
        st.error("Could not generate questions. Please try again.")
        return

    # Display Questions
    for i, q in enumerate(questions):

        st.markdown(f"### Q{i+1}. {q['question']}")

        choice = st.radio(
            label=f"Choose answer for question {i+1}",
            options=q["options"],
            key=f"mcq_{i}"
        )

        st.session_state.mcq_answers[i] = choice

    st.markdown("---")

    # Submit Button
    if st.button("Submit Quiz", use_container_width=True):

        score = 0

        for i, q in enumerate(questions):

            user_ans = st.session_state.mcq_answers.get(i, "")

            correct_ans = q["answer"]

            if user_ans == correct_ans:

                score += 1

                st.success(f"Q{i+1} — Correct!")

            else:

                st.error(
                    f"Q{i+1} — Wrong. Correct answer: {correct_ans}"
                )

            st.caption(f"Explanation: {q['explanation']}")

        # Final Score
        st.markdown("---")
        st.markdown(f"# 🎯 Your Score: {score} / {len(questions)}")
        update_progress(
          score,
          len(questions)
        )
        if score == len(questions):

            st.balloons()

            st.success("Perfect score! Excellent work!")

        elif score >= len(questions) // 2:

            st.info("Good effort! Review the wrong answers above.")

        else:

            st.warning(
                "Keep practicing! Re-read the explanations and try again."
            )