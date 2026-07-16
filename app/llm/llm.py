from ollama import Client


class JarvisLLM:
    def __init__(self, model="llama3.1:8b"):
        self.client = Client(host="http://localhost:11434")
        self.model = model

    def ask(self, messages: list) -> str:
        """
        Send the complete conversation history to Ollama.
        """

        try:
            response = self.client.chat(
                model=self.model,
                messages=messages
            )

            return response["message"]["content"]

        except Exception as e:
            print(f"LLM Error: {e}")
            return "Sorry, I couldn't process your request."