from pathlib import Path


def load_documents():
    project_root = Path(__file__).parent.parent
    folder = project_root / "data" / "documents"

    files = folder.iterdir()

    documents = []

    for file in files:
        if file.suffix == ".txt":
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()

            document = {
                "text": text,
                "source": file.name
            }

            documents.append(document)

    return documents


if __name__ == "__main__":
    documents = load_documents()
    print(documents)