import whisper


class SpeechToText:
    """
    Speech-to-Text using OpenAI Whisper.
    """

    def __init__(self, model_name="small"):
        """
        Load the Whisper model.

        Available models:
        - tiny
        - base
        - small   (Recommended)
        - medium
        - large
        """

        print("=" * 50)
        print("Loading Whisper model...")
        print("=" * 50)

        self.model = whisper.load_model(model_name)

        print(f"✅ Whisper '{model_name}' model loaded successfully.")

    def transcribe(self, audio_path):
        """
        Convert speech audio into text.
        """

        print("\n📝 Transcribing audio...")

        try:

            result = self.model.transcribe(
                audio_path,
                language="en",
                fp16=False,
                temperature=0,
                beam_size=5,
                best_of=5,
                verbose=False
            )

            text = result["text"].strip()

            if not text:
                return ""

            print(f"📝 Recognized Text: {text}")

            return text

        except Exception as e:

            print(f"❌ Transcription Error: {e}")

            return ""