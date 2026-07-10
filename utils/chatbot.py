from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import (
    create_embeddings,
    create_query_embedding
)
from utils.vector_store import (
    create_vector_store,
    search_vector_store
)
from utils.llm import generate_answer


def process_pdf(uploaded_file):
    text = extract_text(uploaded_file)

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    vector_store = create_vector_store(embeddings)

    return chunks, embeddings, vector_store


def retrieve_chunks(question, vector_store, chunks):

    query_embedding = create_query_embedding(question)

    indices = search_vector_store(
        vector_store,
        query_embedding
    )

    retrieved_chunks = []

    for idx in indices:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks

def answer_question(question, vector_store, chunks):

    retrieved_chunks = retrieve_chunks(
        question,
        vector_store,
        chunks
    )

    answer = generate_answer(
        question,
        retrieved_chunks
    )

    return answer, retrieved_chunks