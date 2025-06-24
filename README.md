# Smart Resume Screener

An AI-powered tool for HR to upload resumes (PDFs), summarize them, and match them against job descriptions using NLP.

## Features

- Upload PDF resumes and job descriptions
- Extracts and summarizes resume content
- Scores and ranks resumes based on job description match
- Simple web interface (Streamlit)

## Tech Stack

- **Backend:** FastAPI, PyMuPDF, scikit-learn, HuggingFace Transformers
- **Frontend:** Streamlit

## Quick Start

1. **Clone the repo and set up a virtual environment:**
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt

2. **Run the backend:**
   uvicorn backend.backend_api:app --reload --port 9000

3. **Run the frontend:**
   streamlit run frontend/front.py --server.port 8501

4. **Open your browser:**  
   Go to (http://localhost:8501)

## Folder Structure

ai-resume-parser/
├── backend/
├── frontend/
├── resumes/
├── requirements.txt
└── README.md

## License

Open source, for educational and non-commercial use.
