def build_prompt(context, question):

    return f"""
You are an expert AI assistant.

Answer the user's question using ONLY the information provided in the context.

Do not answer unrelated information.

Context:
{context}

Question:
{question}

Provide a direct answer to the question.
"""