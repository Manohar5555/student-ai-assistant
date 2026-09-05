import numpy as np

from src.embeddings import create_embeddings


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve(query, vector_store, top_k=2, min_score=0.45):
    query_embedding = create_embeddings([query])[0]

    results = []


    for item in vector_store:
        score = cosine_similarity(
            query_embedding,
            item["embedding"]
        )


        if score >= min_score:
            results.append({
                "text": item["text"],
                "source": item["source"],
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]


if __name__ == "__main__":
    print("Retriever module working")