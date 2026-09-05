class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def clear(self):
        self.messages = []

if __name__ == "__main__":

    memory = ConversationMemory()

    memory.add_message({
        "role": "user",
        "content": "What is the attendance requirement?"
    })

    memory.add_message({
        "role": "assistant",
        "content": "The minimum attendance is 75%."
    })

    print(memory.get_messages())