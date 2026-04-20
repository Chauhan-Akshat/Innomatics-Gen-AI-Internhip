import os
import sys
import json
import re
from dotenv import load_dotenv
from langsmith import traceable
from langchain_groq import ChatGroq

from chains.extract_chain import create_extract_chain
from chains.explain_chain import create_explain_chain
from utils.matcher import match_skills


# Base setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))

groq_api_key = os.getenv("GROQ_API_KEY")
print("API Key Loaded:", groq_api_key is not None)


# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key
)

extract_chain = create_extract_chain(llm)
explain_chain = create_explain_chain(llm)


# Helpers
def safe_json_parse(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {"skills": []}
    except:
        return {"skills": []}


def load_file(path):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        raise Exception(f"❌ File NOT FOUND: {full_path}")
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()


# Pipeline
@traceable
def run_pipeline(resume, job_description, name):
    print(f"\n=========== {name.upper()} ===========")

    extracted = extract_chain.invoke({"resume": resume})
    extracted_data = safe_json_parse(extracted)
    print("Extracted:", extracted_data)

    match_data = match_skills(extracted_data, job_description)
    print("Match:", match_data)

    explanation = explain_chain.invoke({
        "matched_skills": match_data["matched_skills"],
        "missing_skills": match_data["missing_skills"],
        "score": match_data["score"]
    })

    print("Explanation:\n", explanation)


# Run
if __name__ == "__main__":

    print("FILES IN ROOT:", os.listdir(BASE_DIR))

    jd = load_file("job_description.txt")

    # Check folder exists
    if not os.path.exists(os.path.join(BASE_DIR, "resumes")):
        raise Exception("❌ 'resumes' folder not found")

    print("Resume Files:", os.listdir(os.path.join(BASE_DIR, "resumes")))

    strong = load_file("resumes/strong_resume.txt")
    avg = load_file("resumes/average_resume.txt")
    weak = load_file("resumes/weak_resume.txt")

    run_pipeline(strong, jd, "Strong Candidate")
    run_pipeline(avg, jd, "Average Candidate")
    run_pipeline(weak, jd, "Weak Candidate")