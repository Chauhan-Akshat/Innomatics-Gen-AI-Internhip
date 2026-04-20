from langchain_core.output_parsers import StrOutputParser
from prompts.match_prompt import match_prompt


def create_match_chain(llm):
    chain = match_prompt | llm | StrOutputParser()
    return chain