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

    st.subheader("Your Information")

    st.write(f"**Name:** {name}")
    st.write(f"**Education:** {education}")
    st.write(f"**Skills:** {skills}")
    st.write(f"**Career Goal:** {career_goal}")
    st.write(f"**Interests:** {interests}")