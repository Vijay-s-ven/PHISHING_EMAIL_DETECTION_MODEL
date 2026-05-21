# Phishing Email Detection Model

A Machine Learning based Phishing Email Detection System built using Python and Scikit-learn that classifies emails as **Phishing** or **Safe** based on textual content, suspicious keywords, and URL analysis.

---

## Project Overview

Phishing emails are fraudulent messages designed to steal sensitive information such as passwords, banking details, and personal data. This project uses Machine Learning techniques to automatically detect phishing emails with high accuracy.

The model analyzes:
- Email text content
- Suspicious keywords
- Presence of URLs
- Fraud-related patterns

and predicts whether an email is:
- ⚠️ Phishing
- ✅ Safe

---

## Features

- Train on phishing and legitimate email datasets
- Extract email features using TF-IDF
- Detect suspicious URLs and keywords
- Machine Learning classification using Random Forest
- Accuracy evaluation
- Confusion Matrix visualization
- Interactive user input testing

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

---

## Project Structure

```bash
PHISHING_EMAIL_DETECTION/
│
├── phishing_detector.py
├── emails.csv
├── requirements.txt
└── README.md
