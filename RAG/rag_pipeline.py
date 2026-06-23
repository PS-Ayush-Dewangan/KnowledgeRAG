from opentelemetry import context

from Retrieval.retriever import retrieve_documents
from LLM.llm_utils import get_llm
from RAG.prompt_builder import build_prompt
from Sources.wikipedia_loader import load_wikipedia
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store


def ask_wikipedia(question):
    text = load_wikipedia(question)
    chunks = create_chunks(text)
    create_vector_store(chunks)
    return ask_rag(question)


def ask_rag(question):

    documents = retrieve_documents(
        query=question,
        k=7
    )

    context = "\n\n".join(
    f"Context {i+1}:\n{doc.page_content}"
    for i, doc in enumerate(documents)
)

    print("\n===== RETRIEVED CONTEXT =====")
    print(context[:3000])
    print("\n=============================")
    prompt = build_prompt(
        context=context,
        question=question
    )

  
    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content