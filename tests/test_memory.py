from app.assistant.conversation import ConversationManager
from app.llm.llm import JarvisLLM


def main():
    conversation = ConversationManager()
    llm = JarvisLLM()

    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        conversation.add_user_message(user_input)

        response = llm.ask(conversation.get_messages())

        conversation.add_assistant_message(response)

        print(f"\nJarvis: {response}\n")


if __name__ == "__main__":
    main()