print("AI Powered Phishing Detector Started 🚀") 

import pandas as pd
import numpy as np 

print("Libraries Imported Successfully 😎") 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 

print("Machine Learning Ready 🔥") 

data = {
    'url_length': [10, 50, 75, 20, 90],
    'has_https': [1, 1, 0, 1, 0],
    'has_at_symbol': [0, 0, 1, 0, 1],
    'is_phishing': [0, 0, 1, 0, 1]
} 

df = pd.DataFrame(data) 

print(df) 

X = df[['url_length', 'has_https', 'has_at_symbol']]
y = df['is_phishing'] 

model = RandomForestClassifier() 

model.fit(X, y) 

print("AI Model Trained Successfully 🚀") 

test_url = [[80, 0, 1]] 

prediction = model.predict(test_url) 

if prediction[0] == 1:
    print("❌ Phishing Website Detected")
else:
    print("✅ Safe Website") 

test_url = [[15, 1, 0]] 

prediction = model.predict(test_url) 

if prediction[0] == 1:
    print("❌ Phishing Website Detected")
else:
    print("✅ Safe Website")
# ==========================
# ADVANCED URL ANALYZER
# ==========================

def extract_features(url):

    url_length = len(url)

    has_https = 1 if url.startswith("https") else 0

    has_at_symbol = 1 if "@" in url else 0

    dot_count = url.count(".")

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "paypal",
        "gift",
        "free",
        "bonus"
    ]

    suspicious_score = 0

    for word in suspicious_words:
        if word in url.lower():
            suspicious_score += 1

    return {
        "url_length": url_length,
        "has_https": has_https,
        "has_at_symbol": has_at_symbol,
        "dot_count": dot_count,
        "suspicious_score": suspicious_score
    }


print("\n==========================")
print("AI URL ANALYZER")
print("==========================")

user_url = input("Enter URL: ")

features = extract_features(user_url)

print("\nExtracted Features:")
print(features)

risk_score = 0

risk_score += features["url_length"] // 10

risk_score += features["has_at_symbol"] * 25

risk_score += features["suspicious_score"] * 10

if features["has_https"] == 0:
    risk_score += 20

risk_score = min(risk_score, 100)

print(f"\nThreat Score: {risk_score}/100")

if risk_score >= 70:
    print("🚨 HIGH RISK PHISHING WEBSITE")
elif risk_score >= 40:
    print("⚠️ SUSPICIOUS WEBSITE")
else:
    print("✅ SAFE WEBSITE")
