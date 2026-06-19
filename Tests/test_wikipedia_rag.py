from Sources.wikipedia_loader import load_wikipedia
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store


topic = "Artificial intelligence"

text = load_wikipedia(topic)

chunks = create_chunks(text)

print(f"Total Chunks: {len(chunks)}")

vector_store = create_vector_store(chunks)

print("Wikipedia data stored in FAISS successfully")