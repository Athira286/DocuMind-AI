import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS index from document embeddings.
    """

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index

def search_vector_store(index, query_embedding, k=3):
    """
    Search the FAISS index for the top k similar chunks.
    """

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    return indices[0]