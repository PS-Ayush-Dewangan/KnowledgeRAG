from pinecone import (
    Pinecone,
    ServerlessSpec
)

from config.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

existing_indexes = [
    index["name"]
    for index in pc.list_indexes()
]

if PINECONE_INDEX_NAME not in existing_indexes:

    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

print(
    "Pinecone Connected Successfully"
)

print(
    pc.list_indexes()
)