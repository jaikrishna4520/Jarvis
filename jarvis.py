from app.assistant.assistant import Assistant


def main():
    try:
        jarvis = Assistant()

        print("\n🚀 JARVIS is ready!")

        jarvis.run()

    except KeyboardInterrupt:
        print("\n👋 Shutting down JARVIS...")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()