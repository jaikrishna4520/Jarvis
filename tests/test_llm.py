from app.llm.llm import JarvisLLM


def main():
    llm = JarvisLLM()

    while True:
        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = llm.ask(question)

        print("\nJarvis:", answer)


if __name__ == "__main__":
    main()