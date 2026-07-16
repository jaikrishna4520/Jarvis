from app.tts.tts import TextToSpeech


def main():

    tts = TextToSpeech()

    tts.speak(
        "Hello Jayakrishna. I am Jarvis. Nice to meet you."
    )


if __name__ == "__main__":
    main()