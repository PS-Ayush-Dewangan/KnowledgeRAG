from Sources.website_loader import load_website
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store

url = "https://fastapi.tiangolo.com/"

text = load_website(url)

chunks = create_chunks(text)

print(f"Chunks Created: {len(chunks)}")

create_vector_store(chunks)

print("Website data stored in FAISS")