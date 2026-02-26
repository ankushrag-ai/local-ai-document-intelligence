import streamlit as st
from pypdf import PdfReader
import requests

st.set_page_config(page_title="PDF Summarizer (Ollama)", layout="wide")
st.title("📄 PDF Summarizer (Local - Ollama)")

# Extract text from PDF
def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Send text to Ollama
def summarize_with_ollama(text):
    prompt = f"""
Summarize the following PDF content.

Return:
- Title
- Executive Summary (5 lines)
- Key Points (10 bullets)
- Key Takeaways (5 bullets)

TEXT:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        pdf_text = extract_text(uploaded_file)

    if st.button("Summarize"):
        with st.spinner("Summarizing with Ollama..."):
            summary = summarize_with_ollama(pdf_text[:15000])  # limit size for now

        st.markdown(summary)