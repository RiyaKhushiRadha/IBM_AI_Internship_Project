import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.role_recommender import recommend_roles
from utils.skill_extractor import extract_skills

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

    # Resume Parsing
    resume_text = extract_text_from_pdf(uploaded_file)

    # st.subheader("📄 Extracted Resume Text")

    # st.text_area(
    #     "Resume Content",
    #     resume_text,
    #     height=300
    # )

    # Skill Extraction
    skills = extract_skills(resume_text)

    st.subheader("🛠 Extracted Skills")

    if skills:

        for skill in skills:
            st.write(f"• {skill}")

    else:
        st.warning("No skills detected.")

    # Role Recommendation
    recommendations = recommend_roles(skills)

    st.subheader("🎯 Recommended Roles")

    if recommendations:

        for role, score in recommendations:
            st.write(
                f"**{role}** → Match Score: {score:.0f}%"
            )

    else:
        st.warning(
            "No matching roles found."
        )