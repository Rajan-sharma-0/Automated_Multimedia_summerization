# helpers/extract_text_from_pdf.py

import PyPDF2

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from PDF.
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text
