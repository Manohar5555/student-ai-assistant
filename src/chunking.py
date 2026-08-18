def chunk_text(text, chunk_size=10, overlap=2):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text) - chunk_size + 1, step):
        chunks.append(text[i:i + chunk_size])

    return chunks


if __name__ == "__main__":
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        text,
        chunk_size=10,
        overlap=2
    )

    print(chunks)