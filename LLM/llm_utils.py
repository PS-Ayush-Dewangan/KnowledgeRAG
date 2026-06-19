from langchain_ollama import ChatOllama


MODEL_NAME = "llama3.2:1b"


def get_llm():

    llm = ChatOllama(
        model=MODEL_NAME
    )

    return llm