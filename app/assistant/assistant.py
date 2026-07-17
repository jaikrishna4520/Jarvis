from app.speech.audio import AudioRecorder
from app.speech.wakeword import WakeWordDetector
from app.speech.stt import SpeechToText
from app.llm.llm import JarvisLLM
from app.tts.tts import TextToSpeech
from app.assistant.conversation import ConversationManager
from app.core.router import route


class Assistant:

    def __init__(self):

        print("=" * 60)
        print("🤖 Initializing JARVIS...")
        print("=" * 60)

        # ----------------------------------
        # Initialize Modules
        # ----------------------------------

        self.audio = AudioRecorder()

        self.wakeword = WakeWordDetector()

        # Better accuracy than "base"
        self.stt = SpeechToText(
            model_name="small"
        )

        self.llm = JarvisLLM()

        self.conversation = ConversationManager()

        self.tts = TextToSpeech(
            voice="en-IN-PrabhatNeural"
        )

        print("\n✅ All modules initialized successfully.")

    # =====================================================

    def wait_for_wake_word(self):

        print("\n😴 Waiting for wake word...")

        self.wakeword.start()

        print("\n👂 Wake word detected!")

    # =====================================================

    def listen_for_command(self):

        print("\n🎤 Listening for your command...")

        audio_file = self.audio.record(

            duration=6,

            output_file="temp/command.wav"

        )

        return audio_file

    # =====================================================

    def transcribe(self, audio_file):

        print("\n📝 Transcribing...")

        text = self.stt.transcribe(audio_file)

        if not text:

            return ""

        text = text.strip()

        print(f"\n👤 You said: {text}")

        return text

    # =====================================================

    def think(self, prompt):

        print("\n🧠 Thinking...")

        self.conversation.add_user_message(prompt)

        response = self.llm.ask(

            self.conversation.get_messages()

        )

        self.conversation.add_assistant_message(

            response

        )

        print("\n🤖 Jarvis:")

        print(response)

        return response

    # =====================================================

    def speak(self, response):

        if not response:

            return

        print("\n🔊 Speaking...")

        self.tts.speak(response)

    # =====================================================

    def run(self):

        print("\n🚀 JARVIS is Online!")

        print("Say the wake word to activate me.\n")

        exit_words = [

            "exit",

            "quit",

            "bye",

            "goodbye",

            "good bye",

            "stop jarvis",

            "shutdown jarvis"

        ]

        while True:

            try:

                # ----------------------------------
                # Wait for Wake Word
                # ----------------------------------

                self.wait_for_wake_word()

                # ----------------------------------
                # Record Audio
                # ----------------------------------

                audio_file = self.listen_for_command()

                # ----------------------------------
                # Speech To Text
                # ----------------------------------

                text = self.transcribe(audio_file)

                if not text:

                    print("\n❌ No speech detected.")

                    continue

                text = text.lower().strip()

                print(f"\n📥 Command : {text}")

                # ----------------------------------
                # Exit
                # ----------------------------------

                if any(

                    word in text

                    for word in exit_words

                ):

                    goodbye = "Goodbye! Have a great day."

                    print(f"\n👋 {goodbye}")

                    self.speak(goodbye)

                    break

                # ----------------------------------
                # Local Router
                # ----------------------------------

                response = route(text)

                if response:

                    print("\n⚡ Local command executed.")

                else:

                    print("\n🌐 Sending request to AI...")

                    response = self.think(text)

                # ----------------------------------
                # Speak
                # ----------------------------------

                self.speak(response)

                print("\n" + "=" * 60)

            except KeyboardInterrupt:

                print("\n👋 Interrupted by user.")

                break

            except Exception as e:

                print(f"\n❌ Error: {e}")