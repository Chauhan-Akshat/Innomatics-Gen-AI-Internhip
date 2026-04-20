from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI resume analyzer.

Extract the following information from the resume.

Return ONLY valid JSON.

{{
 "skills": [],
 "tools": [],
 "experience_years": number
}}

Resume:
{resume}

Rules:
- Do NOT assume skills not present
- Extract only explicitly mentioned information
"""
)