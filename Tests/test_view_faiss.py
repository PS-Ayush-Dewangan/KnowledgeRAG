from VectorDB.vector_store import load_vector_store

vector_store = load_vector_store()

print(
    f"Total Chunks: {len(vector_store.docstore._dict)}"
)

for i, doc in enumerate(
    vector_store.docstore._dict.values(),
    start=1
):

    print(f"\nChunk {i}")
    print("-" * 50)
    print(doc.page_content[:500])