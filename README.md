# AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions and provides ATS-style insights such as skill matching, missing keywords, and improvement suggestions.

---

## 🔍 Features
- Upload resume in PDF format
- Paste job description
- Extracts text from resume automatically
- Provides ATS score, matched skills, missing skills, and recommendations
- Clean and simple web interface

---

## 🛠️ Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS
- PDF Processing: PyPDF2
- AI Integration: OpenAI API (mocked during development)
- Environment Management: python-dotenv

---

## ⚙️ Workflow
1. User uploads resume and enters job description  
2. Flask backend receives inputs  
3. Resume text is extracted from PDF  
4. AI prompt is generated for ATS-style analysis  
5. Structured JSON response is displayed on the UI  

---

## 🚀 How to Run Locally

```bash
pip install flask PyPDF2 openai python-dotenv
python app.py

📌 Notes

AI responses were mocked during development to avoid API rate limits.

The architecture supports easy switching to live OpenAI API calls.

👩‍💻 Author

Shivali Gupta


👉 Save the file.

This README is **internship-level professional**.

---

# 🟢 PART 3: PUSH TO GITHUB (STEP-BY-STEP)

## 🔹 Step 3.1: Create GitHub Repository

1. Go to 👉 https://github.com
2. Click **New repository**
3. Repository name:


ai-resume-analyzer

4. Description (optional):


AI-powered resume analyzer using Flask and OpenAI

5. Public
6. Click **Create repository**

Leave the page open.

---

## 🔹 Step 3.2: Initialize Git Locally

Back in VS Code → Terminal:

```powershell
git init
git add .
git commit -m "Initial commit: AI Resume Analyzer"
