import streamlit as st
from utils import read_pdf
from backend import add_resume, match_resumes
from groq_client import analyze_resume

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("🧠 AI Resume Matcher (Groq-powered)")

# Upload resumes
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        text = read_pdf(file)
        add_resume(text, file.name)
    st.success(f"{len(uploaded_files)} resumes indexed successfully!")

# Job description
st.subheader("📌 Job Description")
job_desc = st.text_area("Paste job description here")

if st.button("Match Resumes") and job_desc:
    results = match_resumes(job_desc)

    st.subheader("🔍 Top Matches")
    for i in range(len(results["ids"][0])):
        st.write(f"**{i+1}. {results['ids'][0][i]}**")

    st.subheader("🧠 AI Analysis (Best Match)")
    report = analyze_resume(job_desc, results["documents"][0][0])
    st.write(report)
