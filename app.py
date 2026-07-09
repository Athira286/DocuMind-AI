import streamlit as st

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

    st.success("PDF uploaded successfully!")

    text = extract_text(uploaded_file)

    st.subheader("Extracted Text Preview")

    st.write(text[:1000])