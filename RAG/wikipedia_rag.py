from Sources.wikipedia_loader import load_wikipedia
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store
from RAG.rag_pipeline import ask_rag


def ask_wikipedia(question):

    article = load_wikipedia(question)

    if not article:
        return "No Wikipedia article found."

    chunks = create_chunks(article)

    create_vector_store(chunks)

    answer = ask_rag(question)

    return answer