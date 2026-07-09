import streamlit as st

from utils.chatbot import (
    process_pdf,
    retrieve_chunks
)

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

        chunks, embeddings, vector_store = process_pdf(uploaded_file)

    st.success("✅ PDF processed successfully!")

    st.subheader("📊 Document Statistics")

    st.write(f"Total Chunks: {len(chunks)}")

    st.write(f"Embedding Shape: {embeddings.shape}")

    with st.expander("Preview First Chunk"):
        st.write(chunks[0])

    st.subheader("🗂️ Vector Store")

    st.success("FAISS index created successfully!")

    st.subheader("❓ Ask a Question")

    question = st.text_input(
        "Ask something about the PDF"
    )

    if question:

        retrieved_chunks = retrieve_chunks(
            question,
            vector_store,
            chunks
        )

        st.subheader("📄 Retrieved Chunks")

        for i, chunk in enumerate(retrieved_chunks):

            st.write(f"### Result {i+1}")

            st.write(chunk)

            st.divider()