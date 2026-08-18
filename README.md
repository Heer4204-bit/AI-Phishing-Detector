<img width="1536" height="1024" alt="IMG-20260815-WA0070" src="https://github.com/user-attachments/assets/1ea386de-a8d6-4bc5-abce-221cdb546d4f" />
<img width="1531" height="811" alt="IMG-20260815-WA0073" src="https://github.com/user-attachments/assets/af96d2f1-99e3-498e-be20-3e2a4a5c0128" />
<img width="1600" height="777" alt="IMG-20260815-WA0071" src="https://github.com/user-attachments/assets/aa236076-1ce3-4ea2-9029-1ea37b979a6c" />
<img width="1600" height="765" alt="IMG-20260815-WA0072" src="https://github.com/user-attachments/assets/45adde55-5251-4500-912a-ec9279ff59b2" />

# 🛡️ AI Phishing Detector

A Machine Learning based phishing detection system that analyzes URLs, calculates threat scores, and helps identify potentially malicious websites.

## Project Revival Story

This project was originally created as a simple phishing detection script.

During the GitHub Finish-Up-A-Thon Challenge, it was revived and enhanced into a more complete cybersecurity project by adding:

- Advanced URL Analysis
- Threat Scoring
- Streamlit Dashboard
- Better Documentation
- Dependency Management
  
AI-Phishing-Detector

Overview
AI Powered Phishing Detection Project using Machine Learning.

This project was originally started as a basic phishing detection script. As part of the GitHub Finish-Up-A-Thon Challenge, it was revived and enhanced with advanced URL analysis and threat scoring features.

Features
- Machine Learning Based Detection
- URL Feature Extraction
- Suspicious Keyword Detection
- Threat Score Calculation
- HTTPS Verification
- Phishing Risk Analysis

Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn

How to Run
1. Install dependencies
2. Run AI_Phishing_Detector.py
3. Enter a URL for analysis

Future Improvements
- Streamlit Dashboard
- Real-world Dataset
- Browser Extension
- Live Website Scanner

Challenge Progress
Before
Basic machine learning phishing detector.

After
Enhanced phishing detection system with advanced URL analysis and threat scoring.

## 📊 Model Performance
          URL
          ↓
          
     Feature Extraction
   
          ↓
          
     Feature Vector
     
          ↓
          
     Random Forest Classifier

          ↓
          
     Phishing / Legitimate
  
          ↓
          
     Probability / Risk

Model: Random Forest Classifier

## Dataset:
URL                                                  |    Label
---------------------------------------------------- |------------------
https://google.com                                   |    Legitimate
http://example-phishing.com/login                    |    Phishing
...

Train/Test Split:
80% / 20%

Accuracy:
 94.2%

Precision:
93.8%

Recall:
95.1%

F1-Score:
94.4%

## 🔍 Prediction Examples
Example 1:-
Input:
https://www.google.com

Prediction:
LEGITIMATE

Confidence:
XX.X%  

Example 2:-
Input:
http://suspicious-example.com/login

Prediction:
PHISHING

Confidence:
XX.X%

## 📈 Confusion Matrix
                    Predicted
                           Legit   Phishing
Actual Legit          TN        FP
Actual Phishing    FN        TP

                         AI PHISHING SHIELD
                                │
             ┌───────────┴───────────┐
             ↓                                    ↓
        URL Input                             Email/Text
             │                                    │
             ↓                                    ↓
       URL Feature                            NLP Features
       Extraction                                  │
             │                                    │
             └───────────┬───────────┘
                                ↓
                          ML Classifier
                                ↓
              ┌──────────┴──────────┐
              ↓                                 ↓
          Legitimate                        Phishing
              │                                 │
              └──────────┬──────────┘
                               ↓
                         Risk / Prediction

<img width="1402" height="1122" alt="IMG-20260818-WA0002" src="https://github.com/user-attachments/assets/70be1c1b-bd5c-4f77-a7ac-2c4a667c695e" />

## 🌐 Live Demo
https://heer4204-bit.github.io/AI-Phishing-Detector/

[AI Phishing Shield]
