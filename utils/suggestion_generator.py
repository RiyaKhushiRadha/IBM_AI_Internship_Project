def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Learn {skill.title()}"
        )

    suggestions.append(
        "Build at least 2 projects in your target domain"
    )

    suggestions.append(
        "Complete a relevant certification"
    )

    return suggestions