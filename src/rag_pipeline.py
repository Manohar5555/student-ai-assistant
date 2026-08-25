from src.retriever import retrieve
from src.context_builder import build_context
from src.prompt_builder import build_prompt
from src.generator import generate_answer


def ask(query, vector_store):
    results = retrieve(query, vector_store)

    context = build_context(results)

    prompt = build_prompt(query, context)

    answer = generate_answer(prompt)

    return answer


if __name__ == "__main__":
    print("RAG pipeline module working")