from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_description = request.form.get("jd")

        # 1. Extract resume text from PDF
        reader = PdfReader(resume_file)
        resume_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

        # 2. Mock AI response (final, stable version)
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

        # 3. Convert AI JSON string → Python dict
        analysis = json.loads(ai_result)

        # 4. Send structured data to result page
        return render_template(
            "result.html",
            score=analysis["ats_score"],
            matched=analysis["matched_skills"],
            missing=analysis["missing_skills"],
            suggestions=analysis["suggestions"]
        )

    # GET request → show landing page
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
