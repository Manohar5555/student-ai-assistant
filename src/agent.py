import os
import json

from dotenv import load_dotenv
from groq import Groq

from src.tools import rag_tool, calculator_tool
from src.memory import ConversationMemory


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API")
)
memory = ConversationMemory()

tools = [
    {
        "type": "function",
        "function": {
            "name": "rag_tool",
            "description": "Search college documents for information about college policies, courses, placements, attendance, leave, and other student-related information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The question to search for in the college documents."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator_tool",
            "description": "Perform mathematical calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression such as 25 * 40."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def run_agent(query):

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful college student assistant.

Rules:
1. Use rag_tool when the user asks about college information, policies, attendance, placement, leave, fees, courses, or other information that may be present in college documents.
2. Use calculator_tool when the user asks for a mathematical calculation.
3. Always use the appropriate tool when the user's question requires information from college documents or a mathematical calculation.
4. If a question requires both college information and a calculation, use the necessary tools before answering.
5. When using rag_tool, use only the information returned by the tool.
6. Do not add general knowledge or assumptions to college-related answers.
7. If the tool does not provide the requested information, say you don't know based on the provided documents.
8. If a tool returns success=True, use the information in its result to answer the user.
9. If a tool returns success=False, do not pretend the tool succeeded. Explain the error clearly.
10. Give a clear and concise final answer.
"""
        }
    ]

    messages.extend(memory.get_messages())

    messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    while True:

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                tools=tools,
                tool_choice="auto",
                temperature=0
            )

        except Exception:
            return "Unable to process the request right now."

        message = response.choices[0].message

        if not message.tool_calls:

            memory.add_message({
                "role": "user",
                "content": query
            })

            memory.add_message({
                "role": "assistant",
                "content": message.content
            })

            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:


            try:

                if tool_call.function.name == "rag_tool":

                    arguments = json.loads(
                        tool_call.function.arguments
                    )

                    tool_result = rag_tool(
                        arguments["query"]
                    )

                elif tool_call.function.name == "calculator_tool":

                    arguments = json.loads(
                        tool_call.function.arguments
                    )

                    tool_result = calculator_tool(
                        arguments["expression"]
                    )

                else:
                    tool_result = {
                        "success": False,
                        "result": None,
                        "error": "Unknown tool"
                    }

            except Exception:
                tool_result = {
                    "success": False,
                    "result": None,
                    "error": "Tool execution failed."
                }

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_result)
                }
            )

