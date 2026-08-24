import numpy as np


def create_vector_store(chunks, embeddings):
    vector_store = []

    for chunk, embedding in zip(chunks, embeddings):
        vector_store.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "embedding": embedding
        })

    return vector_store


if __name__ == "__main__":
    chunks = [
        {
            "text": "Students must maintain 75% attendance.",
            "source": "attendance_policy.txt"
        },
        {
            "text": "Students can contact the placement cell.",
            "source": "college_faq.txt"
        }
    ]

    embeddings = np.array([
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6]
    ])

    vector_store = create_vector_store(chunks, embeddings)

    print("Number of vectors:", len(vector_store))
    print(vector_store[0])