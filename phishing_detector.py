import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("emails.csv")

# Encode labels
df['label'] = df['label'].map({'safe': 0, 'phishing': 1})

# Custom feature extractor
class URLFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self

    def transform(self, emails):
        features = []

        for email in emails:
            url_count = len(re.findall(r'http[s]?://', email))
            suspicious_words = len(re.findall(
                r'free|win|winner|bank|verify|urgent|click|password|account',
                email.lower()
            ))

            features.append([url_count, suspicious_words])

        return features

# Features and labels
X = df['text']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Text features
tfidf = TfidfVectorizer(stop_words='english')

# URL & keyword features
url_features = URLFeatureExtractor()

# Transform text
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# URL features
X_train_url = url_features.transform(X_train)
X_test_url = url_features.transform(X_test)

# Combine features
from scipy.sparse import hstack

X_train_combined = hstack([X_train_tfidf, X_train_url])
X_test_combined = hstack([X_test_tfidf, X_test_url])

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_combined, y_train)

# Predictions
y_pred = model.predict(X_test_combined)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Safe', 'Phishing'],
            yticklabels=['Safe', 'Phishing'])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Test custom email
while True:
    test_email = input("\nEnter an email message (or type 'exit'): ")

    if test_email.lower() == 'exit':
        break

    email_tfidf = tfidf.transform([test_email])
    email_url = url_features.transform([test_email])

    email_combined = hstack([email_tfidf, email_url])

    prediction = model.predict(email_combined)[0]

    if prediction == 1:
        print("⚠️ This email is PHISHING")
    else:
        print("✅ This email is SAFE")