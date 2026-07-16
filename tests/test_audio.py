from app.speech.audio import AudioRecorder


def main():
    recorder = AudioRecorder()
    recorder.record(duration=5)


if __name__ == "__main__":
    main()