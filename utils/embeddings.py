import streamlit as st
from sentence_transformers import SentenceTransformer


@st.cache_resource
def load_model():
    """
    Load the embedding model only once.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Generate embeddings for document chunks.
    """
    model = load_model()
    embeddings = model.encode(chunks)

    return embeddings


def create_query_embedding(query):
    """
    Generate an embedding for the user's question.
    """
    model = load_model()
    embedding = model.encode(query)

    return embedding