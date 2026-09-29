import re

SKILLS = [
    "python", "java", "javascript", "typescript", "c", "c++", "c#",
    "html", "css", "react", "node.js", "express", "django", "flask",
    "streamlit", "sql", "mysql", "postgresql", "mongodb",
    "git", "github", "rest api", "api", "json",
    "machine learning", "deep learning", "artificial intelligence",
    "natural language processing", "nlp", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch",
    "data analysis", "power bi", "excel",
    "aws", "azure", "docker", "linux"
]


def extract_skills(text: str) -> list[str]:
    """Find known technical skills in text using case-insensitive matching."""
    normalized = text.lower()
    found = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, normalized):
            found.append(skill)

    return found
