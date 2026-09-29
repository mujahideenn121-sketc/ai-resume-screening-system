from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text: str, job_description: str) -> float:
    """Return a TF-IDF cosine similarity score scaled to 0-100."""
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(float(similarity * 100), 2)
