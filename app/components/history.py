import streamlit as st


def show_history():

    st.markdown("## 🕘 Learning History")

    history = st.session_state.get(
        "history",
        []
    )

    if not history:

        st.info(
            "No learning history yet."
        )

        return

    for item in history[-10:]:

        role = item.get("role", "")

        content = item.get(
            "content",
            ""
        )

        if role == "user":

            st.markdown(
                f"👨‍🎓 **You:** {content}"
            )

        else:

            st.markdown(
                f"🤖 **EduBot:** {content[:300]}..."
            )

        st.markdown("---")