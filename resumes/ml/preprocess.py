#resume_analysis/resumes/ml/preprocess.py
import os
from PyPDF2 import PdfReader
import docx

def extract_text_from_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        reader = PdfReader(path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
    elif ext in [".docx", ".doc"]:
        doc = docx.Document(path)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    return text.strip()
