PHISHING_EMAIL_DETECTION

Simple demo project for detecting phishing emails using a small dataset and a Naive Bayes classifier.

Files
- phishing_detector.py - small training script and interactive predictor
- emails.csv - sample dataset (columns: text,label)
- requirements.txt - Python dependencies

Quick start

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the detector:

```powershell
python phishing_detector.py
```

Type or paste an email body at the prompt to get a prediction (`phishing` or `legitimate`).
