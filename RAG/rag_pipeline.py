from Retrieval.retriever import retrieve_documents

from LLM.llm_utils import get_llm

from RAG.prompt_builder import build_prompt

from Sources.wikipedia_loader import load_wikipedia

from Chunking.chunk_utils import create_chunks

from VectorDB.pinecone_store import (
    create_pinecone_store
)


def ask_wikipedia(question):

    text = load_wikipedia(
        question
    )

    if text is None:

        return "Wikipedia article not found."

    chunks = create_chunks(
        text
    )

    create_pinecone_store(
        chunks,
        source="Wikipedia",
        document=question
    )

    return ask_rag(
        question,
        source="Wikipedia"
    )


def ask_rag(
    question,
    source=None
):

    documents = retrieve_documents(
        query=question,
        source=source,
        k=7
    )

    context = "\n\n".join(

        f"""Context {i+1}

Source: {doc['source']}
Document: {doc['document']}
Chunk: {doc['chunk_number']}

{doc['text']}"""

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

    response = llm.invoke(
        prompt
    )

    return response.content