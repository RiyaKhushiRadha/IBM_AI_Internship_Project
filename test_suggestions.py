from utils.suggestion_generator import generate_suggestions

missing_skills = [
    "power bi",
    "statistics"
]

suggestions = generate_suggestions(
    missing_skills
)

for suggestion in suggestions:
    print(suggestion)