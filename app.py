from flask import Flask, render_template, request
import fitz
from docx import Document

from analyzer import analyze_resume


app = Flask(__name__)


def extract_pdf(file):

    text = ""

    pdf = fitz.open(
        stream=file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text


def extract_docx(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        resume = request.files.get("resume")
        job_description = request.form.get(
            "job_description"
        )

        if not resume:

            error = "Please upload a resume."

            return render_template(
                "index.html",
                error=error
            )

        filename = resume.filename.lower()

        if filename.endswith(".pdf"):

            resume_text = extract_pdf(resume)

        elif filename.endswith(".docx"):

            resume_text = extract_docx(resume)

        else:

            error = "Only PDF and DOCX files are supported."

            return render_template(
                "index.html",
                error=error
            )

        result = analyze_resume(
            resume_text,
            job_description
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)