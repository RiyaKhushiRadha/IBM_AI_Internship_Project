import streamlit as st

st.set_page_config(page_title="Smart Career Assistant", page_icon="🎯")

st.title("🎯 Smart Career Assistant using AI")

st.header("👤 User Profile")

with st.form("profile_form"):
    name = st.text_input("Enter your name")

    education = st.selectbox(
        "Education Level",
        ["High School", "Diploma", "Undergraduate", "Postgraduate"]
    )

    skills = st.text_area(
        "Enter your skills (comma separated)"
    )

    career_goal = st.text_input(
        "What career do you want to pursue?"
    )

    interests = st.text_area(
        "Areas of interest"
    )

    submitted = st.form_submit_button("Generate Profile")

if submitted:
    st.success("Profile Submitted Successfully! 🎉")

    st.subheader("🎯 Career Recommendations")

    skills_lower = skills.lower()
    career_goal_lower = career_goal.lower()

    career_paths = []
    skills_to_learn = []
    certifications = []

    # AI Careers
    if "ai" in career_goal_lower or "machine learning" in career_goal_lower:
        career_paths = [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ]

        skills_to_learn = [
            "Python",
            "Machine Learning",
            "SQL",
            "Deep Learning"
        ]

        certifications = [
            "IBM AI Fundamentals",
            "Google Data Analytics"
        ]

    # Data Careers
    elif "data" in career_goal_lower:
        career_paths = [
            "Data Analyst",
            "Business Analyst",
            "Data Scientist"
        ]

        skills_to_learn = [
            "SQL",
            "Power BI",
            "Tableau",
            "Python"
        ]

        certifications = [
            "Google Data Analytics",
            "IBM Data Analyst"
        ]

    # Web Development Careers
    elif (
        "web" in career_goal_lower
        or "frontend" in career_goal_lower
        or "full stack" in career_goal_lower
    ):
        career_paths = [
            "Frontend Developer",
            "Full Stack Developer",
            "UI Engineer"
        ]

        skills_to_learn = [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js"
        ]

        certifications = [
            "Meta Front-End Developer",
            "JavaScript Certification"
        ]

    else:
        st.info("More recommendations coming soon 🚀")

    # Show recommendations only if careers are found
    if career_paths:

        st.success("Recommended Career Paths")

        for career in career_paths:
            st.write(f"• {career}")

        # Find missing skills
        missing_skills = []

        for skill in skills_to_learn:
            if skill.lower() not in skills_lower:
                missing_skills.append(skill)

        st.subheader("📚 Skills to Learn")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"• {skill}")
        else:
            st.success(
                "🎉 Congratulations! You already have all the required skills."
            )

        st.subheader("🏆 Certifications")

        for cert in certifications:
            st.write(f"• {cert}")