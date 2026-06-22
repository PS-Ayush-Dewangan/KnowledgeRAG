from RAG.rag_pipeline import ask_rag

while True:

    question = input("\nAsk: ")

    if question.lower().strip() == "exit":
        break

    answer = ask_rag(question)

    print("\nAnswer:")
    print(answer)