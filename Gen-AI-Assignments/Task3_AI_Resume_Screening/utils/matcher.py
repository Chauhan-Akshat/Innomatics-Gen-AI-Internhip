def match_skills(extracted_data, job_description):
    """
    Matches extracted resume skills with job description skills
    and returns match details + score.
    """

    # Extract skills safely
    resume_skills = extracted_data.get("skills", [])
    
    # If JD is string → convert to lowercase text
    if isinstance(job_description, str):
        jd_text = job_description.lower()
    else:
        jd_text = str(job_description).lower()

    matched = []
    missing = []

    for skill in resume_skills:
        if skill.lower() in jd_text:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(resume_skills)
    score = round((len(matched) / total) * 100, 2) if total > 0 else 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "score": score
    }