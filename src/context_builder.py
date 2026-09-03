def build_context(results):
    context = ""

    for result in results:
        context += (
            f"Source: {result['source']}\n"
            f"{result['text']}\n\n"
        )

    return context


if __name__ == "__main__":
    results = [
        {
            "text": "Students must maintain a minimum attendance of 75%.",
            "source": "attendance_policy.txt",
            "score": 0.8
        },
        {
            "text": "Students below 65% attendance are normally not eligible.",
            "source": "attendance_policy.txt",
            "score": 0.6
        }
    ]

    context = build_context(results)

    print(context)