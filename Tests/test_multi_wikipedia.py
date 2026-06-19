from Sources.wikipedia_loader import load_wikipedia
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store


topics = [
    "Artificial intelligence",
    "Machine learning",
    "Deep learning",
    "FastAPI",
    "Python (programming language),"
    "Vector databases",
    "Retrieval-Augmented Generation",
    "Natural language processing"
    "LangChain"
    "Ollama",
]

all_chunks = []

for topic in topics:

    print(f"Loading: {topic}")

    text = load_wikipedia(topic)

    if text:

        chunks = create_chunks(text)

        all_chunks.extend(chunks)

        print(f"Added {len(chunks)} chunks")


print(f"\nTotal Chunks: {len(all_chunks)}")

create_vector_store(all_chunks)

print("Knowledge Base Created Successfully")