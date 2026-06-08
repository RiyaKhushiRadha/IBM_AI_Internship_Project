from utils.role_recommender import recommend_roles

skills = [
    "Python",
    "Machine Learning",
    "SQL"
]

recommendations = recommend_roles(skills)

for rec in recommendations:
    print(rec)