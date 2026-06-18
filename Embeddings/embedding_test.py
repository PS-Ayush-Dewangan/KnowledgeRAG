from langchain_ollama import OllamaEmbeddings
from math import sqrt

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

ai_text = "Artificial Intelligence"
ml_text = "Machine Learning"
pizza_text = "Pizza"

ai_vector = embeddings.embed_query(ai_text)
ml_vector = embeddings.embed_query(ml_text)
pizza_vector = embeddings.embed_query(pizza_text)


def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    magnitude1 = sqrt(sum(a * a for a in vec1))
    magnitude2 = sqrt(sum(b * b for b in vec2))

    return dot_product / (magnitude1 * magnitude2)


print(
    "AI vs ML:",
    cosine_similarity(ai_vector, ml_vector)
)

print(
    "AI vs Pizza:",
    cosine_similarity(ai_vector, pizza_vector)
)