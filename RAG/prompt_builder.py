def build_prompt(context, question):

    return f"""
You are an expert AI assistant.

Answer the user's question using the provided context.

Focus on the most relevant information.

Context:
{context}

Question:
{question}

Answer:
"""