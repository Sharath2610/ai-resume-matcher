import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(job_desc, resume_text):
    prompt = f"""
You are an ATS Resume Screening AI.

Job Description:
{job_desc}

Candidate Resume:
{resume_text}

Provide:
1. Match score (0-100)
2. Key strengths
3. Missing skills
4. Final hiring recommendation
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
