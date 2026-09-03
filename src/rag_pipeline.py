from src.retriever import retrieve
from src.context_builder import build_context
from src.prompt_builder import build_prompt
from src.generator import generate_answer


def ask(query, vector_store):
    results = retrieve(query, vector_store)

    if not results:
        return {
            "answer": "I don't know based on the provided documents.",
            "sources": []
        }

    context = build_context(results)

    prompt = build_prompt(query, context)

    answer = generate_answer(prompt)

    sources = list(set(result["source"] for result in results))

    return {
        "answer": answer,
        "sources": sources
    }

if __name__ == "__main__":
    print("RAG pipeline module working")