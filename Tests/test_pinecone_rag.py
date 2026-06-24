from RAG.rag_pipeline import ask_rag

question = input("Ask: ")

answer = ask_rag(
    question
)

print("\nAnswer:")
print(answer)