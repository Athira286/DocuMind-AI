import streamlit as st
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.pdf_loader import extract_text
from utils.vector_store import create_vector_store
from utils.embeddings import create_query_embedding
from utils.vector_store import search_vector_store

st.set_page_config(
    page_title="Chat with PDF",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Chat with PDF")

st.write("Upload a PDF and I'll read it.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with st.spinner("📖 Processing your PDF..."):

        text = extract_text(uploaded_file)

        chunks = split_text(text)

        embeddings = create_embeddings(chunks)

        vector_store = create_vector_store(embeddings)

    st.success("✅ PDF processed successfully!")

    st.subheader("Document Statistics")
    
    st.write(f"Total Chunks: {len(chunks)}")

    st.write(f"Embedding Shape: {embeddings.shape}")
    with st.expander("Preview First Chunk"):
        st.write(chunks[0])
    
    st.subheader("Vector Store")
    st.success("FAISS index created successfully!")
    st.subheader("Ask a Question")
    question = st.text_input(
        "Ask something about the PDF"
    )
    if question:
        query_embedding = create_query_embedding(question)
        indices = search_vector_store(
            vector_store,
            query_embedding
        )
        st.subheader("Retrieved Chunks")
        for idx in indices:
            st.write(f"### Chunk {idx+1}")
            st.write(chunks[idx])
            st.divider()
