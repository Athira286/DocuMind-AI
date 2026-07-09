import streamlit as st
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.pdf_loader import extract_text


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

    st.success("✅ PDF processed successfully!")

    st.subheader("Document Statistics")
    
    st.write(f"Total Chunks: {len(chunks)}")

    st.write(f"Embedding Shape: {embeddings.shape}")
    with st.expander("Preview First Chunk"):
        st.write(chunks[0])

    for i, chunk in enumerate(chunks):

        st.subheader(f"Chunk {i+1}")

        st.write(chunk)