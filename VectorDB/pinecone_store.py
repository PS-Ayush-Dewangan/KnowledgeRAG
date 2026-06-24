import uuid

from pinecone import Pinecone
from langchain_ollama import OllamaEmbeddings

from config.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
)

EMBEDDING_MODEL = "mxbai-embed-large"


def get_embeddings():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def create_pinecone_store(chunks, source, document):
    embeddings = get_embeddings()

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)

    vectors = []
    for i, chunk in enumerate(chunks):
        vector = embeddings.embed_query(chunk)
        vectors.append(
            {
                "id": str(uuid.uuid4()),
                "values": vector,
                "metadata": {
                    "text": str(chunk),
                    "source": str(source),
                    "document": str(document),
                    "chunk_number": int(i),
                },
            }
        )

    index.upsert(vectors=vectors)
    print(f"{len(vectors)} chunks uploaded to Pinecone")


def retrieve_documents(query, source=None, k=3):
    embeddings = get_embeddings()
    query_embedding = embeddings.embed_query(query)

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)

    if source:
        results = index.query(
            vector=query_embedding,
            top_k=k,
            include_metadata=True,
            filter={"source": source}
        )
    else:
        results = index.query(
            vector=query_embedding,
            top_k=k,
            include_metadata=True
        )

    documents = []
    for match in results.matches:
        metadata = match.metadata or {}
        documents.append(
            {
                "text": metadata.get("text", ""),
                "source": metadata.get("source", "Unknown"),
                "document": metadata.get("document", "Unknown"),
                "chunk_number": metadata.get("chunk_number", -1),
            }
        )

    return documents


def get_index_stats():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    return index.describe_index_stats()


def delete_all_vectors():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
    index.delete(delete_all=True)
    print("All vectors deleted from Pinecone")
