def calculate_ats_score(user_skills, required_skills):

    user_skills = [skill.lower() for skill in user_skills]
    required_skills = [skill.lower() for skill in required_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in user_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    ats_score = (
        len(matched_skills) /
        len(required_skills)
    ) * 100

    return {
        "score": round(ats_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }