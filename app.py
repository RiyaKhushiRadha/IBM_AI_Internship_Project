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

if "AI" in career_goal.upper():
    st.success("Recommended Career Paths")
    st.write("• AI Engineer")
    st.write("• Machine Learning Engineer")
    st.write("• Data Scientist")

    st.subheader("📚 Skills to Learn")
    st.write("• Machine Learning")
    st.write("• SQL")
    st.write("• Deep Learning")

    st.subheader("🏆 Certifications")
    st.write("• IBM AI Fundamentals")
    st.write("• Google Data Analytics")

elif "DATA" in career_goal.upper():
    st.success("Recommended Career Paths")
    st.write("• Data Analyst")
    st.write("• Business Analyst")
    st.write("• Data Scientist")

    st.subheader("📚 Skills to Learn")
    st.write("• SQL")
    st.write("• Power BI")
    st.write("• Tableau")

    st.subheader("🏆 Certifications")
    st.write("• Google Data Analytics")
    st.write("• IBM Data Analyst")

else:
    st.info("More recommendations coming soon 🚀")