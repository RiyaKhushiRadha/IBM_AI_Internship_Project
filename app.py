import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.role_recommender import recommend_roles
from utils.ats_matcher import calculate_ats_score
from utils.ai_suggestions import generate_ai_suggestions
from utils.interview_generator import generate_interview_questions

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

    top_role = recommendations[0][0]

    st.subheader("📊 ATS Match Score")

    role_required_skills = [
        "Python",
        "Machine Learning",
        "SQL",
        "Deep Learning",
        "NLP"
    ]

    ats_result = calculate_ats_score(
        skills,
        role_required_skills
    )

    st.metric(
        "ATS Score",
        f"{ats_result['score']}%"
    )

    st.write("✅ Matched Skills")

    for skill in ats_result["matched_skills"]:
        st.write(f"• {skill}")

    st.write("❌ Missing Skills")

    for skill in ats_result["missing_skills"]:
        st.write(f"• {skill}")

    st.subheader("💡 AI Suggestions")

    ai_suggestions = generate_ai_suggestions(
        skills,
        top_role,
        ats_result["missing_skills"]
        )

    st.write(ai_suggestions)
    
    questions = generate_interview_questions(
        skills
        )

    st.subheader("🎤 Interview Questions")

    for question in questions:
        st.write(f"❓ {question}")

    # else:
    #     st.warning(
    #         "No matching roles found."
    #     )