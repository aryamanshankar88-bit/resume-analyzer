SKILLS = [
    "python",
    "c",
    "c++",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "node.js",
    "sql",
    "mysql",
    "mongodb",
    "git",
    "github",
    "docker",
    "aws",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data structures",
    "algorithms",
    "flask",
    "django",
    "fastapi",
    "tensorflow",
    "pytorch"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))


def analyze_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = []
    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(job_skills) > 0:
        score = round(
            (len(matched) / len(job_skills)) * 100
        )
    else:
        score = 0

    suggestions = []

    if "git" not in resume_skills:
        suggestions.append(
            "Consider adding Git/GitHub projects."
        )

    if "sql" not in resume_skills:
        suggestions.append(
            "Consider adding SQL or database projects."
        )

    if "data structures" not in resume_skills:
        suggestions.append(
            "Mention Data Structures if you have studied them."
        )

    if len(resume_text.split()) < 150:
        suggestions.append(
            "Your resume appears short. Consider adding relevant projects and achievements."
        )

    return {
        "score": score,
        "resume_skills": resume_skills,
        "matched": matched,
        "missing": missing,
        "suggestions": suggestions
    }