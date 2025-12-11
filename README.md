# AI Resume Matcher (Groq-Powered)

A Generative AI–based web application that evaluates resumes against job descriptions using semantic search and Large Language Model (LLM) reasoning.

---

FEATURES

- Upload resumes in PDF format
- Paste job descriptions
- Semantic similarity matching using embeddings
- AI-generated resume analysis:
  - Match percentage
  - Strengths
  - Missing skills
  - Hiring recommendation
- Interactive UI built with Streamlit
- Cloud-based LLM inference using Groq (LLaMA 3.1)

---

TECH STACK

- Python
- Streamlit
- Groq API (LLaMA 3.1)
- Sentence Transformers
- ChromaDB
- LangChain
- PyPDF

---

PROJECT STRUCTURE

ai-resume-matcher/

- app.py
- groq_client.py
- requirements.txt
- README.md

---

LOCAL SETUP

1. Install dependencies
   pip install -r requirements.txt

2. Run the app
   streamlit run app.py

---

ENVIRONMENT VARIABLES

Create a .env file locally:

GROQ_API_KEY=your_groq_api_key

For deployment, the API key is configured securely in Streamlit Cloud Secrets.

---

USE CASES

- Automated resume screening
- ATS-style candidate evaluation
- AI-assisted hiring tools
- Resume to job description matching

---

DEPLOYMENT

This application is deployed using Streamlit Community Cloud with secure API key handling.

---

AUTHOR

Sharath R
AI / Data Science Enthusiast
