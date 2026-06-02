import streamlit as st
from pypdf import PdfReader

from core.simplifier import generate_explanation


def extract_pdf_text(uploaded_file):

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


def show_pdf_upload():

    st.markdown("---")
    st.subheader("Upload Notes / PDF")

    uploaded_file = st.file_uploader(
        "Upload educational PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("PDF uploaded successfully!")

        if st.button("Simplify Uploaded Notes"):

            with st.spinner("Reading PDF and simplifying content..."):

                pdf_text = extract_pdf_text(uploaded_file)

                simplified = generate_explanation(
                    topic=pdf_text[:3000],
                    level=st.session_state.get("student_level", "Beginner"),
                    style=st.session_state.get("learning_style", "Step-by-step learner")
                )

                st.markdown("## Simplified Notes")
                st.markdown(simplified)