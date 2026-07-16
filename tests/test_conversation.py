from app.assistant.conversation import ConversationManager


def main():
    conversation = ConversationManager()

    conversation.add_user_message("Hello")

    conversation.add_assistant_message("Hi! I am Jarvis.")

    conversation.add_user_message("What is AWS?")

    conversation.print_history()


if __name__ == "__main__":
    main()