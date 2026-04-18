responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm just code, but I'm running fine.",
    "bye": "Goodbye!",
    "what is ai": "AI means making computers do tasks that seem to need human thinking.",
}


def reply(message):
    message = message.lower().strip()
    for keyword, answer in responses.items():
        if keyword in message:
            return answer
    return "I don't know that one yet."


if __name__ == "__main__":
    print("Chatbot ready. Type 'bye' to exit.")
    while True:
        text = input("You: ")
        answer = reply(text)
        print(f"Bot: {answer}")
        if "bye" in text.lower():
            break
