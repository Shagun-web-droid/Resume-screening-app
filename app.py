from flask import Flask, render_template, request
import pdfplumber

from nlp.skill_matcher import extract_skills
from nlp.ml_matcher import match_resume_job

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return render_template("index.html", error="No file uploaded")

    file = request.files["resume"]
    job_desc = request.form["job_description"]

    resume_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text() or ""

    skills = extract_skills(resume_text)
    score = match_resume_job(resume_text, job_desc)

    return render_template(
        "index.html",
        skills=skills,
        score=score
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)

