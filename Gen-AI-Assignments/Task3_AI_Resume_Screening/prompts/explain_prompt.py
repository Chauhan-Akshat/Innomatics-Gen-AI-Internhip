from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "matched_skills", "missing_skills"],
    template="""
Explain the candidate evaluation.

Score:
{score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Provide a short explanation for the recruiter.
"""
)