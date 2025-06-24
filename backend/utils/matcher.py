from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, jd_text):
    documents = [resume_text, jd_text]
    tfidf = TfidfVectorizer().fit_transform(documents)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(float(score) * 100, 2)