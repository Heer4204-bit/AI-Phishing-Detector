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
