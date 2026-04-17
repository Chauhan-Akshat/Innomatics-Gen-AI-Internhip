# Mini Prompt Engine using LangChain

## Overview

This project was built as part of a **GenAI Internship** and demonstrates how to create a flexible and reusable prompt system using LangChain.

Instead of relying on fixed prompts, this implementation uses **PromptTemplate** and **ChatPromptTemplate** to generate structured and adaptable prompts for real-world AI applications.

---

## Objective

* Replace hardcoded prompts with reusable templates
* Build dynamic prompt generation systems
* Design practical LLM-based prompt pipelines

---

## Tech Stack

* Python
* LangChain
* Groq (LLM)

---

## Features Implemented

### Task 1: Basic PromptTemplate

* Designed a reusable template for generating simple explanations

### Task 2: Multi-Input Prompt System

* Handled multiple inputs such as `topic`, `audience`, and `tone`

### Task 3: Prompt Variations Engine

* Generated prompts in different styles:

  * Teaching
  * Interview
  * Storytelling

### Task 4: ChatPromptTemplate

* Implemented role-based prompts:

  * Teacher
  * Interviewer
  * Motivator

### Task 5: Input Validation

* Added validation with default values
* Improved system reliability

### Task 6: Prompt Generator Function

* Built a function to dynamically generate prompts based on style

### Task 7: Template Reusability

* Showcased how a single template can support multiple inputs

---

## Pipeline Flow

User Input → Validation → Prompt Template → Model → Output

---

## How to Run

1. Install dependencies:

   ```
   pip install langchain langchain-groq
   ```

2. Open the notebook in Jupyter or Google Colab

3. Enter your Groq API key when prompted

4. Run all cells

---

## Key Learnings

* Designing reusable prompt templates
* Managing multi-input prompt systems
* Using role-based prompting with ChatPromptTemplate
* Implementing validation for robust pipelines
* Building scalable prompt engineering workflows

---

## Future Improvements

* Add a user interface
* Integrate with web applications
* Expand prompt styles and use cases

---

## Author

**Akshat Chauhan**

---

## Internship Note

This project was completed as part of a **GenAI Internship – Prompt Engineering Assignment using LangChain**.