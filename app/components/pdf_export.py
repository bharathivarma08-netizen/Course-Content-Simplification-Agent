import streamlit as st
from fpdf import FPDF
import os


def create_pdf(content):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    lines = content.split("\n")

    for line in lines:

        try:

            pdf.multi_cell(
                0,
                10,
                txt=line
            )

        except:

            pass

    output_path = "student_notes.pdf"

    pdf.output(output_path)

    return output_path


def show_pdf_download():

    if "last_explanation" not in st.session_state:
        return

    st.markdown("---")

    st.markdown("## 📄 Download Notes")

    if st.button(
        "Generate PDF Notes",
        use_container_width=True
    ):

        with st.spinner(
            "Creating PDF..."
        ):

            content = st.session_state.get(
                "last_explanation",
                ""
            )

            pdf_path = create_pdf(
                content
            )

        with open(
            pdf_path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇ Download PDF",
                data=file,
                file_name="EduBot_Notes.pdf",
                mime="application/pdf",
                use_container_width=True
            )