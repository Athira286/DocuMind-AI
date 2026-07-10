import streamlit as st
from pypdf import PdfReader

@st.cache_data
def extract_text(pdf_file):
    """
    Extract text from all pages of a PDF.
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text