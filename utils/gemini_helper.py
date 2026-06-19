import google.generativeai as genai
import streamlit as st

genai.configure(
<<<<<<< HEAD
    api_key=st.secrets["GEMINI_API_KEY"]
=======
    api_key="AQ.Ab8RN6K4UoBiW6nWt0yu2X_mC72TJM153TTWKmEw2tsEuM5FYA"
>>>>>>> a1a5cb0 (Prepare app for deployment using Streamlit secrets)
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_gemini_response(prompt):

    try:

        response = model.generate_content(prompt)

        print("Gemini response:")
        print(response.text)

        return response.text

    except Exception as e:

        print("Gemini Error:")
        print(e)

        return "Unable to generate response right now."
