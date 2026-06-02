import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        .stButton>button {
            border-radius: 12px;
            height: 3em;
            font-size: 16px;
            font-weight: 600;
        }

        .stTextInput>div>div>input {
            border-radius: 10px;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        h1, h2, h3 {
            font-weight: 700;
        }

        </style>
        """,
        unsafe_allow_html=True
    )