import pandas as pd


def recommend_roles(user_skills):

    df = pd.read_csv("naukri_data_science_jobs_india.csv")

    recommendations = {}

    user_skills = [skill.lower() for skill in user_skills]

    for _, row in df.iterrows():

        job_role = str(row["Job_Role"])

        skills_text = str(row["Skills/Description"]).lower()

        matched_skills = 0

        for skill in user_skills:
            if skill in skills_text:
                matched_skills += 1

        if matched_skills > 0:

            # Calculate match percentage
            match_percentage = (
                matched_skills / len(user_skills)
            ) * 100

            # Clean role name
            clean_role = job_role.split("|")[0].split("/")[0].strip()
            clean_role = job_role.split("|")[0].strip()
            clean_role = clean_role.replace("Sr ", "Senior ")
            clean_role = clean_role.replace("Sr.", "Senior ")
            
            # Keep highest score if duplicate role exists
            if (
                clean_role not in recommendations
                or match_percentage > recommendations[clean_role]
            ):
                recommendations[clean_role] = match_percentage

    # Sort by match percentage
    sorted_roles = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Return top 3
    return sorted_roles[:3]