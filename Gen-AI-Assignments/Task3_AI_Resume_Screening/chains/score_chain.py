from langchain_core.output_parsers import StrOutputParser
from prompts.score_prompt import score_prompt


def create_score_chain(llm):
    chain = score_prompt | llm | StrOutputParser()
    return chain