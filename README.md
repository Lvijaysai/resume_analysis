# resume_analysis
# 🧠 Resume Analysis (Django + Hugging Face)

A secure Django web app that analyzes resumes using NLP models from Hugging Face — built with local model caching and production-grade security.

The app supports PDF, DOCX, DOC, and TXT files up to 5MB, extracts text, generates a concise summary, and ranks roles such as Software Engineer, Data Scientist, or AI Engineer based on content analysis.

## 🚀 Features
- Secure file uploads
- Text extraction using PyPDF2 and python-docx libraries
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

## 🧠 Models Used

| Task | Model | License |
|------|--------|----------|
| **Summarization** | [`sshleifer/distilbart-cnn-12-6`](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | Apache 2.0 |
| **Zero-shot Classification** | [`MoritzLaurer/deberta-v3-small-zeroshot-v1`](https://huggingface.co/MoritzLaurer/deberta-v3-small-zeroshot-v1) | MIT |

> Models used under open-source licenses for educational and portfolio purposes.


output:

Predicted Role: Software Engineer

Summary:
Experienced developer with strong knowledge in backend APIs, database design, and deploying scalable systems.

Role Probabilities:
Software Engineer: 0.71
Backend Developer: 0.18
AI Engineer: 0.06
Frontend Developer: 0.03
Data Scientist: 0.02

