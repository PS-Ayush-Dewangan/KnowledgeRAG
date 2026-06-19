from VectorDB.vector_store import load_vector_store


def retrieve_documents(query, k=3):

    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        query,
        k=k
    )

    return results