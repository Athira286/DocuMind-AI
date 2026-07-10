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

st.markdown("""
<style>

/* Main content width */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:4rem;
    padding-right:4rem;
}

/* Main Title */
h1{
    font-size:3rem !important;
    font-weight:800 !important;
    color:#FAFAFA;
    margin-bottom:0.2rem;
}

/* Section headings */
h2{
    font-size:2rem !important;
    font-weight:700 !important;
    margin-top:1.5rem;
}

/* Smaller headings */
h3{
    font-size:1.4rem !important;
    font-weight:600 !important;
}

/* Normal text */
p, label, div{
    font-size:17px !important;
    line-height:1.7;
}

/* Sidebar */
[data-testid="stSidebar"]{
    padding-top:1rem;
}

/* Buttons */
.stButton>button{
    border-radius:10px;
    font-weight:600;
    height:45px;
}

/* Text Input */
.stTextInput input{
    border-radius:10px;
    font-size:17px;
    padding:12px;
}

</style>
""", unsafe_allow_html=True)

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

/* Hide only menu and footer */
#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

/* Keep the header visible so the sidebar toggle works */
header {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="
font-size:40px;
font-weight:800;
margin-bottom:0;
">
📚 DocuMind-AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
font-size:18px;
color:#9ca3af;
margin-top:0;
">
Chat with any PDF using Retrieval-Augmented Generation (RAG) and Gemini AI.
</p>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.divider()

st.sidebar.markdown("## 📄 Upload Document")
st.sidebar.markdown("""
<div style="
display:flex;
justify-content:center;
align-items:center;
margin:8px 0 18px 0;
">
<h2 style="
margin:0;
font-weight:700;
text-align:center;
">
📄 DocuMind AI
</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()
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



    st.markdown("""
    <h2 style="font-size:34px;font-weight:700;">
    ❓ Ask a Question about your document
    </h2>
    """, unsafe_allow_html=True)

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
        
        st.markdown("""
        <h2 style="font-size:30px;font-weight:700;">
        Response
        </h2>
        """, unsafe_allow_html=True)
        
        st.markdown(
            f"""
        <div style="
        padding:24px;
        border-radius:12px;
        background:#1f2937;
        border:1px solid #333;
        font-size:18px;
        line-height:1.8;
        ">
        {answer}
        </div>
        """,
        unsafe_allow_html=True)
        
        with st.expander("📄 Source Chunks"):
            for i, chunk in enumerate(retrieved_chunks):
                st.markdown(f"### 📄 Retrieved Context {i+1}")
                st.info(chunk)
                st.divider()