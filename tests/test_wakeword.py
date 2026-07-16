from app.speech.wakeword import WakeWordDetector


def main():
    detector = WakeWordDetector()
    detector.start()


if __name__ == "__main__":
    main()