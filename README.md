# resume_analysis
# 🧠 Resume Analysis (Django + Hugging Face)

A secure Django web app that analyzes resumes using NLP models from Hugging Face — built with local model caching and production-grade security.

## 🚀 Features
- Secure file uploads (.pdf, .docx, .txt)
- Hugging Face summarization + zero-shot classification
- Local cache for offline inference
- Django best practices (CSRF, HSTS, HTTPS ready)
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
