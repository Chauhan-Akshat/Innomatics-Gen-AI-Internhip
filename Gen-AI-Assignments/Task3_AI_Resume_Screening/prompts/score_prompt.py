from langchain_core.prompts import PromptTemplate
score_prompt = PromptTemplate(
    input_variables=["matched_skills", "missing_skills"],
    template="""
Based on the matched and missing skills assign a score between 0 and 100.

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Return JSON:

{{
 "score": number
}}
"""
)