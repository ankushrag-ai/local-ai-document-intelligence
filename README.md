\# Local AI Document Intelligence System



A fully local, zero-cost AI-powered document analysis tool built using Streamlit and Ollama.



\## Overview



This project enables users to upload PDF documents and generate structured summaries using a locally hosted large language model (LLM). The system runs entirely offline without external API calls.



\## Features



\- PDF text extraction

\- Structured AI-generated summaries

\- Local LLM inference using Ollama

\- No cloud dependency

\- Zero API cost

\- Streamlit web interface



\## Tech Stack



\- Python

\- Streamlit

\- Ollama (LLM runtime)

\- Phi-3 / Llama3 models

\- PyPDF



\## Architecture



User → Streamlit UI → PDF Text Extraction → Local LLM (Ollama) → Structured Output



\## Why This Project



This project demonstrates:



\- Local LLM integration

\- Prompt engineering

\- REST-based model interaction

\- Document parsing pipelines

\- CPU-based AI deployment

\- End-to-end AI application development



\## Future Improvements



\- Chunk-based processing for large documents

\- Retrieval-Augmented Generation (RAG)

\- Question-answering over documents

\- Multi-document comparison

\- Structured data extraction

\- Performance benchmarking



\## How to Run



1\. Install Ollama

2\. Pull model: `ollama pull phi3`

3\. Create virtual environment

4\. Install dependencies: `pip install -r requirements.txt`

5\. Run: `streamlit run app.py`



---



Built as a learning project to explore local AI application development.

