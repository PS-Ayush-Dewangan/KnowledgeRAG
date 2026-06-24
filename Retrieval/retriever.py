from VectorDB.pinecone_store import (
    retrieve_documents as retrieve_from_pinecone
)


def retrieve_documents(
    query,
    source=None,
    k=3
):

    return retrieve_from_pinecone(
        query=query,
        source=source,
        k=k
    )
