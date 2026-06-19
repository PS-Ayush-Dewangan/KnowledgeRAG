from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


def create_vector_store(chunks):

    embeddings = OllamaEmbeddings(
        model="mxbai-embed-large"
    )

    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_db