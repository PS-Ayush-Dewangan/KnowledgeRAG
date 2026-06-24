from VectorDB.pinecone_store import (
    retrieve_documents
)

results = retrieve_documents(
    "What is Artificial Intelligence?"
)

for i, doc in enumerate(results):

    print(f"\nResult {i+1}")
    print("-" * 50)
    print(doc)