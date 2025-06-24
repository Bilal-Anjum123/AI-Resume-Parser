import streamlit as st
import requests

st.title("Smart Resume Screener")

jd = st.text_area("Paste Job Description (JD) here")
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze") and resume_file and jd:
    files = {"resume": resume_file}
    data = {"jd": jd}
    with st.spinner("Analyzing..."):
        response = requests.post("http://localhost:9000/upload-resume", files=files, data=data)
        if response.ok:
            result = response.json()
            st.subheader("Summary")
            st.write(result["summary"])
            st.subheader("Match Score")
            st.write(f"{result['score']}%")
            st.progress(int(result['score']))
        else:
            st.error("Error processing resume.")