def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]

        if i > 0:
            # Move the beginning forward if it starts in the middle of a word
            first_space = chunk.find(" ")

            if first_space != -1:
                chunk = chunk[first_space + 1:]

        if chunk.strip():
            chunks.append(chunk)

    return chunks


if __name__ == "__main__":
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        text,
        chunk_size=10,
        overlap=2
    )

    print(chunks)