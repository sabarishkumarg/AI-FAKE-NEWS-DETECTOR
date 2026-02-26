from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("AIzaSyBchGmRGLIxr-w_J88tTIrnkLY32xCgDNg"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Page Config
st.set_page_config(
    page_title="Fake News Detector for Students",
    layout="wide"
)

# Header
st.header("📰 Fake News Detector for Students")
st.caption("Analyze articles, detect misinformation, and get trustworthy summaries")

# Sidebar
with st.sidebar:
    st.subheader("📌 Student Info")
    education_level = st.selectbox(
        "Education Level",
        ["High School", "Undergraduate", "Postgraduate"]
    )
    subject = st.text_input("Subject Area (e.g., Politics, Science)")
    st.markdown("---")
    st.info("Paste any news article or link in the main area to analyze credibility.")

# Tabs
tab1, tab2, tab3 = st.tabs(["News Analysis", "Credibility Report", "AI Summary"])

# Session state
if "analysis" not in st.session_state:
    st.session_state.analysis = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "score" not in st.session_state:
    st.session_state.score = ""

# -------- TAB 1: News Input --------
with tab1:
    st.subheader("🔍 Analyze News Article")

    article_text = st.text_area(
        "Paste the news article content here",
        height=250,
        placeholder="Paste full news article or social media post..."
    )

    if st.button("Analyze Article"):
        if not article_text.strip():
            st.warning("Please paste a news article first.")
        else:
            with st.spinner("Analyzing content for credibility..."):
                prompt = f"""
You are an AI fake news detection assistant for students.

Analyze the following article and provide:
1. Credibility score (0–100)
2. Whether the article is likely FAKE or REAL
3. Reasons for your judgment
4. Warning signs of misinformation

Article:
{article_text}
"""
                response = model.generate_content(prompt)
                st.session_state.analysis = response.text

                # Summary prompt
                summary_prompt = f"""
Summarize the following article in a clear, student-friendly way
without spreading misinformation.

Article:
{article_text}
"""
                summary_response = model.generate_content(summary_prompt)
                st.session_state.summary = summary_response.text

# -------- TAB 2: Credibility Report --------
with tab2:
    st.subheader("📊 Credibility Assessment")

    if st.session_state.analysis:
        st.markdown(st.session_state.analysis)
    else:
        st.info("Analyze an article to see the credibility report.")

# -------- TAB 3: AI Summary --------
with tab3:
    st.subheader("🧠 Trustworthy AI Summary")

    if st.session_state.summary:
        st.markdown(st.session_state.summary)
    else:
        st.info("Analyze an article to generate a safe summary.")