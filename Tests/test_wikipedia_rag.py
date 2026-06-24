from Sources.wikipedia_loader import load_wikipedia

from Chunking.chunk_utils import create_chunks

from VectorDB.pinecone_store import (
    create_pinecone_store
)

topic = "Artificial Intelligence"

text = load_wikipedia(
    topic
)

chunks = create_chunks(
    text
)

print(
    f"Total Chunks: {len(chunks)}"
)

create_pinecone_store(
    chunks,
    source="Wikipedia",
    document=topic
)

print(
    "Wikipedia data stored in Pinecone successfully"
)