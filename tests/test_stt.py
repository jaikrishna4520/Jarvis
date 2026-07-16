from app.speech.audio import AudioRecorder
from app.speech.stt import SpeechToText


def main():
    recorder = AudioRecorder()

    audio_file = recorder.record(
        duration=5,
        output_file="temp/command.wav"
    )

    stt = SpeechToText(model_name="base")

    text = stt.transcribe(audio_file)

    print("\n============================")
    print("You said:")
    print(text)
    print("============================")


if __name__ == "__main__":
    main()