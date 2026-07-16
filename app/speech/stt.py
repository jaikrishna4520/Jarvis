import whisper


class SpeechToText:
    def __init__(self, model_name="base"):
        """
        Load the Whisper speech-to-text model.
        """

        print("Loading Whisper model...")

        self.model = whisper.load_model(model_name)

        print(f"Whisper '{model_name}' model loaded successfully.")

    def transcribe(self, audio_path):
        """
        Convert speech audio into text.
        """

        print("Transcribing audio...")

        try:
            result = self.model.transcribe(
                audio_path,
                language="en",      # Change to "te" if speaking Telugu
                fp16=False,         # Prevent CPU warning
                verbose=False
            )

            text = result["text"].strip()

            if not text:
                return "I couldn't understand what you said."

            return text

        except Exception as e:
            print(f"Transcription Error: {e}")
            return ""