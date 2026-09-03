def chunk_text(text, chunk_size=100, overlap=20):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between 0 and chunk_size")

    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk_words = words[i:i + chunk_size]

        if not chunk_words:
            break

        chunk = " ".join(chunk_words)
        chunks.append(chunk)

        if i + chunk_size >= len(words):
            break

    return chunks


if __name__ == "__main__":
    text = """
    Attendance Policy

    Students must maintain a minimum attendance of 75% to be eligible
    for semester examinations.

    Students with attendance between 65% and 74% may apply for condonation
    according to college rules.

    Students below 65% attendance are normally not eligible for the
    semester examination.
    """

    chunks = chunk_text(
        text,
        chunk_size=20,
        overlap=5
    )

    for chunk in chunks:
        print("-----")
        print(chunk)