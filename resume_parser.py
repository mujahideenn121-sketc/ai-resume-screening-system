from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from all readable pages of an uploaded PDF."""
    reader = PdfReader(uploaded_file)
    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return "\n".join(pages).strip()
