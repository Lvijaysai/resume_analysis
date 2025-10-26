# resume_analysis
# 🧠 Resume Analysis (Django + Hugging Face)

A secure Django web app that analyzes resumes using NLP models from Hugging Face — built with local model caching and production-grade security.

## 🚀 Features
- Secure file uploads (.pdf, .docx, .txt)
- Hugging Face summarization + zero-shot classification
- Local cache for offline inference
- Clean UI and responsive design

## 🛠️ Setup
```bash
git clone https://github.com/<your_username>/resume_analysis.git
cd resume_analysis
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
python manage.py runserver
