from utils.interview_generator import generate_interview_questions

skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

questions = generate_interview_questions(
    skills
)

for q in questions:
    print(q)