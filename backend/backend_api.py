from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.utils.resume_parser import extract_text_from_pdf
from backend.utils.matcher import compute_similarity
from transformers import pipeline
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_tokens=900):
    # Simple chunking by words (not tokens, but works for most cases)
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i+max_tokens])

@app.post("/upload-resume")
async def upload_resume(resume: UploadFile = File(...), jd: str = Form(...)):
     # Define the path to save the uploaded resume
    resume_path = f"resumes/{resume.filename}"
    # Save the uploaded file
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
    # Now you can use resume_path
    resume_text = extract_text_from_pdf(resume_path)
    # Summarize in chunks
    summaries = []
    for chunk in chunk_text(resume_text):
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    # Optionally, summarize the summaries
    final_summary = summarizer(" ".join(summaries), max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    # Score
    score = compute_similarity(resume_text, jd)
    return {
        "summary": final_summary,
        "score": score
    }