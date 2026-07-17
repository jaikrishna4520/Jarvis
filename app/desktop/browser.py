import subprocess
import shutil
import webbrowser
import urllib.parse
import os


class Browser:

    def __init__(self):

        self.chrome_path = self.find_chrome()

    def find_chrome(self):

        chrome = shutil.which("chrome")

        if chrome:
            return chrome

        possible_paths = [

            r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

            os.path.expandvars(
                r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
            )
        ]

        for path in possible_paths:

            if os.path.exists(path):
                return path

        return None

    def open_chrome(self):

        if self.chrome_path:

            subprocess.Popen([self.chrome_path])

            return "Opening Chrome."

        webbrowser.open("https://www.google.com")

        return "Opening default browser."

    def open_incognito(self):

        if self.chrome_path:

            subprocess.Popen([self.chrome_path, "--incognito"])

            return "Opening Chrome in Incognito mode."

        return "Google Chrome is not installed."

    def google_search(self, query):

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for {query}"

    def youtube_search(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching YouTube for {query}"

    def open_youtube(self):

        webbrowser.open("https://youtube.com")

        return "Opening YouTube."

    def open_chatgpt(self):

        webbrowser.open("https://chat.openai.com")

        return "Opening ChatGPT."

    def open_gmail(self):

        webbrowser.open("https://mail.google.com")

        return "Opening Gmail."

    def open_github(self):

        webbrowser.open("https://github.com")

        return "Opening GitHub."

    def open_linkedin(self):

        webbrowser.open("https://linkedin.com")

        return "Opening LinkedIn."

    def open_stackoverflow(self):

        webbrowser.open("https://stackoverflow.com")

        return "Opening Stack Overflow."

    def open_aws_console(self):

        webbrowser.open("https://console.aws.amazon.com")

        return "Opening AWS Console."


browser = Browser()


def open_chrome():
    return browser.open_chrome()


def open_incognito():
    return browser.open_incognito()


def google_search(query):
    return browser.google_search(query)


def youtube_search(query):
    return browser.youtube_search(query)


def open_youtube():
    return browser.open_youtube()


def open_chatgpt():
    return browser.open_chatgpt()


def open_gmail():
    return browser.open_gmail()


def open_github():
    return browser.open_github()


def open_linkedin():
    return browser.open_linkedin()


def open_stackoverflow():
    return browser.open_stackoverflow()


def open_aws_console():
    return browser.open_aws_console()