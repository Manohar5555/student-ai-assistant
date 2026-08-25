from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

if __name__ == "__main__":
    texts = [
        "Students must maintain 75% attendance.",
        "Students can contact the placement cell."
    ]

    embeddings = create_embeddings(texts)

    print("Number of embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))