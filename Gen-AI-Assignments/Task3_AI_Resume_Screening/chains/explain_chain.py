from langchain_core.output_parsers import StrOutputParser
from prompts.explain_prompt import explain_prompt


def create_explain_chain(llm):
    chain = explain_prompt | llm | StrOutputParser()
    return chain