from utils.gemini_helper import get_gemini_response

prompt = """
Give me 3 tips to become a Data Scientist.
"""

response = get_gemini_response(
    prompt
)

print(response)