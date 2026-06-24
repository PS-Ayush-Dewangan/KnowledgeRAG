from Chunking.chunk_utils import create_chunks

from VectorDB.pinecone_store import (
    create_pinecone_store
)

text = """
Artificial Intelligence is the capability of a computer system
to perform tasks that normally require human intelligence.
"""

chunks = create_chunks(
    text
)

create_pinecone_store(
    chunks
)