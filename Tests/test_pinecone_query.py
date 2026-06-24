from pinecone import Pinecone

from config.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)

from langchain_ollama import OllamaEmbeddings

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pc.Index(
    PINECONE_INDEX_NAME
)

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

query_vector = embeddings.embed_query(
    "What is Artificial Intelligence?"
)

results = index.query(
    vector=query_vector,
    top_k=3,
    include_metadata=True
)

print(results)