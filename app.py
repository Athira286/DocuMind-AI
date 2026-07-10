import streamlit as st

from utils.chatbot import (
    process_pdf,
    answer_question
)

st.set_page_config(
    page_title="DocuMind-AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='font-size:52px;font-weight:800;margin-bottom:0;'>
DocuMind-AI
</h1>

<p style='font-size:18px;color:#B8B8B8;margin-top:8px;'>
Understand and chat with your PDF documents using Gemini AI and Retrieval-Augmented Generation.
</p>
""", unsafe_allow_html=True)

st.divider()
st.markdown("---")

st.sidebar.markdown("## 📄 Upload Document")
uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with st.spinner("📖 Processing your PDF..."):

        chunks, embeddings, vector_store = process_pdf(uploaded_file)

    st.success("✅ Document ready. You can now start asking questions.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📊 Document Statistics")

    st.sidebar.metric(
        "Total Chunks",
        len(chunks)
    )
    
    st.sidebar.metric(
        "Embedding Dimensions",
        embeddings.shape[1]
    )




    st.markdown("## ❓ Ask a Question")

    question = st.text_input(
        "Ask anything about your document...",
        placeholder="Example: Summarize the report or What are the key findings?"
    )

    if question:

        answer, retrieved_chunks = answer_question(
            question,
            vector_store,
            chunks
        )
        
        st.subheader("Response")
        
        st.markdown(
            f"""
        <div style="
        padding:20px;
        border-radius:12px;
        background:#1e1e1e;
        font-size:18px;
        line-height:1.8;
        ">
        {answer}
        </div>
        """,
        unsafe_allow_html=True)
        
        with st.expander("📄 Source Chunks"):
            for i, chunk in enumerate(retrieved_chunks):
                st.write(f"### Source {i+1}")
                st.write(chunk)
                st.divider()