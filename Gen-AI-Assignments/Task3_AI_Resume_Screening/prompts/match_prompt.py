from langchain_core.prompts import PromptTemplate
match_prompt = PromptTemplate(
    input_variables=["skills", "job_description"],
    template="""
Compare candidate skills with job requirements.

Candidate Skills:
{skills}

Job Description:
{job_description}

Return ONLY JSON:

{{
 "matched_skills": [],
 "missing_skills": []
}}
"""
)