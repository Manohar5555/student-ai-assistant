from src.agent import run_agent


def main():
    print("=================================")
    print("      Student AI Assistant")
    print("=================================")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not query.strip():
            continue

        answer = run_agent(query)

        print("\nAssistant:")
        print(answer)
        print()

if __name__ == "__main__":
    main()