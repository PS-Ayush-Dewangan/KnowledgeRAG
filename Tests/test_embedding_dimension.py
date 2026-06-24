from Embeddings.embedding_utils import get_embeddings

embedding_model = get_embeddings()

vector = embedding_model.embed_query(
    "hello"
)

print(
    len(vector)
)