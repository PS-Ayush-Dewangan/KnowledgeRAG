from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

while True:
    question = input("Ask: ").strip()

    print(f"You entered: '{question}'")  # Debug

    if question.lower() == "exit":
        print("Exiting...")
        break

    response = llm.invoke(question)

    print("\nAnswer:")
    print(response.content)
    print()