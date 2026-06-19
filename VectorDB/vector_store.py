from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


EMBEDDING_MODEL = "mxbai-embed-large"


def create_vector_store(chunks):

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    vector_store.save_local("faiss_index")

    return vector_store


def load_vector_store():

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store