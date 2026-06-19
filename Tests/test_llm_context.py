from LLM.llm_utils import get_llm

llm = get_llm()

response = llm.invoke("""
Context:
Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model.

Question:
What is Retrieval-Augmented Generation?

Answer:
""")

print(response.content)