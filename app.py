import streamlit as st
from utils.parser import extract_text_from_pdf

st.set_page_config(
    page_title="Smart Career Assistant",
    page_icon="🎯"
)

st.title("🎯 Smart Career Assistant using AI")

st.header("📄 Resume Upload")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )