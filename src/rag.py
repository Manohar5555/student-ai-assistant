from src.document_loader import load_documents
from src.chunking import chunk_text
from src.embeddings import create_embeddings
from src.vector_store import create_vector_store
from src.rag_pipeline import ask


def build_vector_store():
    documents = load_documents()

    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["text"])

        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": document["source"]
            })

    embeddings = create_embeddings(
        [chunk["text"] for chunk in all_chunks]
    )

    vector_store = create_vector_store(
        all_chunks,
        embeddings
    )

    return vector_store


def search_college_documents(query):
    vector_store = build_vector_store()

    return ask(query, vector_store)

if __name__ == "__main__":
    result = search_college_documents(
        "What information is available about courses?"
    )

    print(result)