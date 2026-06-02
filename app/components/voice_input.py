import streamlit as st
from streamlit_mic_recorder import mic_recorder


def get_voice_input():

    st.markdown("### 🎤 Voice Input")

    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        just_once=True
    )

    if audio:

        st.success(
            "Voice recorded successfully!"
        )

        st.info(
            "Speech-to-text can be integrated next."
        )

    return audio