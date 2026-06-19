from Retrieval.retriever import retrieve_documents

query = "What is Machine Learning?"

results = retrieve_documents(query)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 30)

    print(doc.page_content)