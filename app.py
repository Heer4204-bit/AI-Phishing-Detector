import streamlit as st

st.set_page_config(page_title="AI Phishing Detector")

st.title("🛡️ AI Phishing Detector")

url = st.text_input("Enter URL")

if st.button("Analyze"):

    score = 0

    if "@" in url:
        score += 25

    if not url.startswith("https"):
        score += 20

    keywords = [
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

    for word in keywords:
        if word in url.lower():
            score += 10

    score = min(score, 100)

    st.metric("Threat Score", score)

    if score >= 70:
        st.error("🚨 High Risk Website")
    elif score >= 40:
        st.warning("⚠️ Suspicious Website")
    else:
        st.success("✅ Safe Website")
