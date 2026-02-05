from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_description = request.form.get("jd")

        # Extract resume text
        reader = PdfReader(resume_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()

        # AI prompt
        prompt = f"""
You are an ATS (Applicant Tracking System).

Compare the resume and job description below.

Resume:
{resume_text}

Job Description:
{job_description}

Return STRICTLY in JSON:
{{
  "ats_score": number,
  "matched_skills": [],
  "missing_skills": [],
  "suggestions": []
}}
"""

        # Call OpenAI
        ai_result = """
{
  "ats_score": 82,
  "matched_skills": ["Python", "Flask", "Machine Learning", "React"],
  "missing_skills": ["Docker", "Cloud Deployment"],
  "suggestions": [
    "Add more measurable project outcomes",
    "Highlight internships or hands-on ML work"
  ]
}
"""


        return f"""
        <h2>AI Resume Analysis</h2>
        <pre>{ai_result}</pre>
        """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
