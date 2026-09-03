def build_prompt(query, context):
    prompt = f"""
You are a helpful college student assistant.

Answer the question using only the provided context.

Rules:
1. Do not use information that is not present in the context.
2. If the answer cannot be found in the context, say "I don't know based on the provided documents."
3. Mention the source document used for the answer.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt

if __name__ == "__main__":
    query = "What is the minimum attendance required?"
    
    context = """
Students must maintain a minimum attendance of 75% to be eligible
for semester examinations.
"""

    prompt = build_prompt(query, context)

    print(prompt)