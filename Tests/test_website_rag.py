from Sources.website_loader import load_website

from Chunking.chunk_utils import create_chunks

from VectorDB.pinecone_store import (
    create_pinecone_store
)

url = "https://fastapi.tiangolo.com/"

text = load_website(
    url
)

chunks = create_chunks(
    text
)

print(
    f"Chunks Created: {len(chunks)}"
)

create_pinecone_store(
    chunks,
    source="Website",
    document=url
)

print(
    "Website data stored in Pinecone successfully"
)