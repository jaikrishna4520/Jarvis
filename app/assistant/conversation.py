from typing import List, Dict


class ConversationManager:
    """
    Manages conversation history for JARVIS.
    """

    def __init__(self):
        self.system_prompt = (
            "You are JARVIS, an advanced AI assistant. "
            "Be professional, concise, friendly, and accurate. "
            "Remember previous conversation context."
        )

        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

    def add_user_message(self, text: str):
        self.messages.append(
            {
                "role": "user",
                "content": text,
            }
        )

    def add_assistant_message(self, text: str):
        self.messages.append(
            {
                "role": "assistant",
                "content": text,
            }
        )

    def get_messages(self):
        return self.messages

    def clear(self):
        """
        Clears conversation while keeping the system prompt.
        """
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

    def print_history(self):
        print("\n========== Conversation ==========")

        for msg in self.messages:
            print(f"{msg['role'].upper()}: {msg['content']}")

        print("==================================\n")