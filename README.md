# IBM_AI_Internship_Project

#  Smart Career Assistant using AI

##  About the Project

Introducing the Smart Career Assistant, an innovative web application powered by AI, designed to support students and job seekers in navigating their career paths. This tool dives into your resume to pull out key skills, suggests job roles that fit you best, checks how well your resume aligns with Applicant Tracking Systems (ATS), generates tailored interview questions, offers tips for career enhancement, and even maps out a personalized career journey using Gemini AI.

The aim of this project is to make career planning a breeze, helping users grasp the skills and preparation needed to land their dream jobs.


##  Features

* Resume Upload and Parsing
* Skill Extraction
* Role Recommendation
* ATS Match Score Analysis
* AI-Powered Career Suggestions
* AI-Generated Interview Questions
* Personalized Career Roadmap


##  Workflow

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Skill Extraction
      ↓
Role Recommendation
      ↓
ATS Match Analysis
      ↓
AI Suggestions
      ↓
Interview Questions
      ↓
Career Roadmap
```


##  Technologies Used

* Python
* Streamlit
* Google Gemini API
* PyPDF2
* Scikit-Learn


##  Project Structure

```text
Smart Career Assistant
│
├── app.py
│
├── utils
│   ├── parser.py
│   ├── skill_extractor.py
│   ├── role_recommender.py
│   ├── ats_matcher.py
│   ├── gemini_helper.py
│   ├── ai_suggestions.py
│   ├── ai_interview_generator.py
│   └── ai_career_roadmap.py
│
├── requirements.txt
├── README.md
└── sample_resume.pdf
```


##  Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move to the project folder

```bash
cd Smart-Career-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```


##  Output

The application offers a range of features to help you on your career journey, including:

* Skills extracted directly from your uploaded resume.
* Job roles that are recommended based on those skills.
* An ATS compatibility score to see how well your resume stands up.
* A list of any skills you might be missing for your desired role.
* AI-generated suggestions for improving your career prospects.
* Interview questions to help you prepare.
* A personalized roadmap to guide your career path.


##  Future Scope

To take the project to the next level, we could consider adding a few enhancements:

* A sleek, modern, and interactive user interface.
* Integration with LinkedIn and various job portals.
* A handy resume builder feature.
* User authentication along with personalized profiles.
* Support for multiple languages.
* Email notifications to keep users updated.
* Tailored learning recommendations for a more personalized experience.
* Cloud deployment paired with seamless database integration.


##  Conclusion

The Smart Career Assistant powered by AI is designed to offer a straightforward yet intelligent platform for career guidance. By merging resume analysis with AI-driven suggestions, interview prep, and personalized career roadmaps, this project empowers users to make informed career choices and get ready for future opportunities with confidence.


##  Developed By

IBM Internship Project

**Smart Career Assistant using AI**

Built using Python, Streamlit, and Gemini AI.
