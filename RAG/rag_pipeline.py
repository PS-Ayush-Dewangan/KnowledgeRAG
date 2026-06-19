from Retrieval.retriever import retrieve_documents
from LLM.llm_utils import get_llm
from RAG.prompt_builder import build_prompt


def ask_rag(question):

    documents = retrieve_documents(
        query=question,
        k=3
    )

    context = "\n\n".join(
    f"Context {i+1}:\n{doc.page_content}"
    for i, doc in enumerate(documents)
)

   
    prompt = build_prompt(
        context=context,
        question=question
    )

  
    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content