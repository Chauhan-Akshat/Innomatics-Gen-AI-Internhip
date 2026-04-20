from langchain_core.output_parsers import StrOutputParser
from prompts.extract_prompt import extract_prompt


def create_extract_chain(llm):
    chain = extract_prompt | llm | StrOutputParser()
    return chain