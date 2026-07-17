from app.speech.audio import AudioRecorder
from app.speech.wakeword import WakeWordDetector
from app.speech.stt import SpeechToText
from app.llm.llm import JarvisLLM
from app.tts.tts import TextToSpeech
from app.assistant.conversation import ConversationManager
from app.core.router import route


class Assistant:
    def __init__(self):
        print("=" * 50)
        print("Initializing JARVIS...")
        print("=" * 50)

        # Initialize all modules
        self.audio = AudioRecorder()
        self.wakeword = WakeWordDetector()
        self.stt = SpeechToText(model_name="base")
        self.llm = JarvisLLM()
        self.conversation = ConversationManager()

        self.tts = TextToSpeech(
            voice="en-IN-PrabhatNeural"
        )

        print("\n✅ All modules loaded successfully!")

    def wait_for_wake_word(self):
        """
        Wait until the wake word is detected.
        """
        print("\n😴 Waiting for wake word...")

        self.wakeword.start()

        print("\n👂 Wake word detected!")

    def listen_for_command(self):
        """
        Record the user's command.
        """
        print("\n🎤 Please speak your command...")

        audio_file = self.audio.record(
            duration=5,
            output_file="temp/command.wav"
        )

        return audio_file

    def transcribe(self, audio_file):
        """
        Convert speech to text.
        """
        print("\n📝 Transcribing...")

        text = self.stt.transcribe(audio_file)

        if text:
            text = text.strip()

        print(f"\n👤 You said: {text}")

        return text

    def think(self, prompt):
        """
        Generate an AI response using conversation memory.
        """
        print("\n🧠 Thinking...")

        # Save user message
        self.conversation.add_user_message(prompt)

        # Ask LLM
        response = self.llm.ask(
            self.conversation.get_messages()
        )

        # Save assistant response
        self.conversation.add_assistant_message(response)

        print(f"\n🤖 Jarvis:\n{response}")

        return response

    def speak(self, response):
        """
        Speak the response.
        """
        if not response:
            return

        print("\n🔊 Speaking...")

        self.tts.speak(response)

    def run(self):
        """
        Main JARVIS loop.
        """
        print("\n🤖 JARVIS is online!")
        print("Say the wake word to activate me.\n")

        exit_words = [
            "exit",
            "quit",
            "bye",
            "goodbye",
            "good bye",
            "stop",
            "stop jarvis",
            "shutdown jarvis"
        ]

        while True:

            try:

                # Wait for wake word
                self.wait_for_wake_word()

                # Listen
                audio_file = self.listen_for_command()

                # Speech to Text
                text = self.transcribe(audio_file)

                if not text:
                    print("❌ No speech detected.")
                    continue

                text = text.lower().strip()

                print(f"\n📥 Command Received: {text}")

                # Exit
                if any(word in text for word in exit_words):

                    goodbye = "Goodbye! Have a great day."

                    print("\n👋", goodbye)

                    self.speak(goodbye)

                    break

                # ==========================================
                # Try Local Command Router First
                # ==========================================

                response = route(text)

                # ==========================================
                # If router doesn't understand,
                # ask the AI model.
                # ==========================================

                if response is None:

                    print("\n🌐 Routing to LLM...")

                    response = self.think(text)

                else:

                    print("\n⚡ Local Command Executed")

                # Speak response

                self.speak(response)

                print("\n" + "=" * 60)

            except KeyboardInterrupt:

                print("\n👋 Interrupted by user.")

                break

            except Exception as e:

                print(f"\n❌ Error: {e}")