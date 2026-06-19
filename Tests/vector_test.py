from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store

with open("data/sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = create_chunks(text)

print(f"Chunks Created: {len(chunks)}")

vector_db = create_vector_store(chunks)

print("Vector Store Created Successfully")