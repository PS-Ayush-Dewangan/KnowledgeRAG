from VectorDB.pinecone_store import delete_all_vectors, get_index_stats

print("Before:", get_index_stats())

delete_all_vectors()

print("After:", get_index_stats())
