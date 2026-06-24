import os
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL = "llama3.2"

EMBEDDING_MODEL = "mxbai-embed-large"

FAISS_PATH = "faiss_index"

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_INDEX_NAME = "knowledge-rag"