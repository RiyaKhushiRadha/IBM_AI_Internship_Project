import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(
    api_key="API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_gemini_response(prompt):

    response = model.generate_content(
        prompt
    )

    return response.text