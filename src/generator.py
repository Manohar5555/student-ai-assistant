import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API")
)


def generate_answer(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    prompt = """
You are a helpful college student assistant.

Answer the question using only the provided context.

Context:
Students must maintain a minimum attendance of 75% to be eligible
for semester examinations.

Question:
What is the minimum attendance required?

Answer:
"""

    answer = generate_answer(prompt)

    print(answer)