#resume_analysis/resumes/ml/analyze.py
import os
import logging
from transformers import pipeline
from .preprocess import extract_text_from_file

logger = logging.getLogger(__name__)

# === Hugging Face Cache Isolation ===
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
os.environ["TRANSFORMERS_CACHE"] = str(BASE_DIR / "hf_cache")

# === File safety constants ===
ALLOWED_EXTENSIONS = ['.pdf', '.docx', '.doc', '.txt']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# === Load ML models ===
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-small-zeroshot-v1")
    logger.info("✅ ML pipelines loaded successfully.")
except Exception as e:
    logger.error(f"❌ Failed to load transformers pipelines: {e}")
    summarizer = None
    classifier = None


def analyze_resume(file_path):
    """Safely extracts text from a resume, summarizes it, and predicts the likely role."""
    try:
        # === File validation ===
        if not os.path.isfile(file_path):
            return {"error": "File does not exist."}

        if os.path.getsize(file_path) > MAX_FILE_SIZE:
            return {"error": "File too large. Max allowed size: 5 MB."}

        ext = os.path.splitext(file_path)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return {"error": f"Unsupported file type: {ext}"}

        # === Extract text ===
        text = extract_text_from_file(file_path)
        if not text.strip():
            return {"error": "No readable text extracted from file."}

        clean_text = " ".join(line.strip() for line in text.splitlines() if line.strip())
        short_text = clean_text[:2000]  # summarizer limit

        # === Summarization ===
        if summarizer:
            try:
                summary = summarizer(short_text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
            except Exception as e:
                logger.warning(f"Summarization failed: {e}")
                summary = "Summary could not be generated."
        else:
            summary = "Summarizer not available."

        # === Classification ===
        labels = ["Software Engineer", "Data Scientist", "Frontend Developer", "Backend Developer", "AI Engineer"]
        if classifier:
            try:
                classification = classifier(clean_text[:1000], labels)
                predicted_role = classification["labels"][0]
                scores = dict(zip(classification["labels"], classification["scores"]))
            except Exception as e:
                logger.warning(f"Classification failed: {e}")
                predicted_role = "Unknown"
                scores = {}
        else:
            predicted_role = "Classifier not available"
            scores = {}

        return {
            "summary": summary,
            "predicted_role": predicted_role,
            "scores": scores,
            "raw_text": clean_text,
        }

    except Exception as e:
        logger.error(f"Error analyzing resume: {e}")
        return {
            "summary": "Analysis failed.",
            "predicted_role": "Error",
            "scores": {},
            "raw_text": "",
        }
