import os


def load_documents():
    folder = "data/documents"

    files = os.listdir(folder)

    documents = []

    for file in files:
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r") as f:
                text = f.read()

            document = {
                "text": text,
                "source": file
            }

            documents.append(document)

    return documents


if __name__ == "__main__":
    documents = load_documents()
    print(documents)