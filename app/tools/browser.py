import webbrowser


def open_chrome():
    """
    Open default browser.
    """
    webbrowser.open("https://www.google.com")
    return "Opening browser..."


def open_youtube():
    webbrowser.open("https://youtube.com")
    return "Opening YouTube..."


def open_chatgpt():
    webbrowser.open("https://chat.openai.com")
    return "Opening ChatGPT..."


def open_gmail():
    webbrowser.open("https://mail.google.com")
    return "Opening Gmail..."