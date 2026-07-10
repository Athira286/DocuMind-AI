# DocuMind-AI

AI-powered PDF Question Answering system built using Retrieval-Augmented Generation (RAG).

## Features

- Upload any PDF
- Semantic search using FAISS
- Sentence Transformers embeddings
- Gemini AI for answer generation
- Source chunk citations
- Cached embeddings for faster loading
- Modern Streamlit UI

## Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- LangChain
- Google Gemini API

## Project Architecture

Upload PDF
↓
Extract Text
↓
Split into Chunks
↓
Create Embeddings
↓
FAISS Vector Store
↓
Semantic Search
↓
Gemini
↓
Answer + Source Chunks

## Installation

```bash
git clone ...
cd DocuMind-AI

pip install -r requirements.txt

streamlit run app.py