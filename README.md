# AI Resume Screening System

An educational AI/NLP-based resume screening application built with Python and Streamlit.

## Features

- Upload a resume in PDF format
- Extract resume text automatically
- Enter a job description
- Calculate resume/job similarity using TF-IDF and cosine similarity
- Detect relevant technical skills
- Show matched skills
- Show potentially missing skills
- Display a simple candidate-alignment analysis
- Clean Streamlit interface

## Tech Stack

- Python
- Streamlit
- Natural Language Processing concepts
- TF-IDF
- Cosine Similarity
- scikit-learn
- pypdf

## Project Structure

```text
ai-resume-screening-system/
├── app.py
├── matcher.py
├── resume_parser.py
├── skills.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate it on Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. The uploaded PDF is converted into text.
2. The resume and job description are transformed into TF-IDF vectors.
3. Cosine similarity is used to calculate a text-alignment score.
4. A built-in technical-skill vocabulary is used to identify matching and potentially missing skills.
5. The results are presented through the Streamlit dashboard.

## Important Limitation

This project is a learning/demo system. It should not be used as the sole basis for employment decisions. The score is affected by wording, formatting, extracted PDF text and the built-in skill vocabulary.

## Author

Mohamed Mujahideen H
B.Sc. Information Technology
