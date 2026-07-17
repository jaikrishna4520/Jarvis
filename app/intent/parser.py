"""
JARVIS Intent Parser
--------------------

Converts natural language into structured intents.
"""

import re


class IntentParser:

    def parse(self, command: str):

        command = command.lower().strip()

        # =====================================
        # Browser
        # =====================================

        if re.search(r"(chrome|browser)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "chrome"
            }

        if re.search(r"(incognito|private)", command):
            return {
                "tool": "browser",
                "action": "incognito"
            }

        if re.search(r"(youtube)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "youtube"
            }

        if re.search(r"(github)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "github"
            }

        if re.search(r"(linkedin)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "linkedin"
            }

        if re.search(r"(gmail)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "gmail"
            }

        if re.search(r"(chatgpt)", command):
            return {
                "tool": "browser",
                "action": "open",
                "target": "chatgpt"
            }

        # =====================================
        # Applications
        # =====================================

        if re.search(r"(vs code|visual studio code|code)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "vscode"
            }

        if re.search(r"(notepad)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "notepad"
            }

        if re.search(r"(calculator|calc)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "calculator"
            }

        if re.search(r"(paint)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "paint"
            }

        if re.search(r"(cmd|command prompt)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "cmd"
            }

        if re.search(r"(powershell)", command):
            return {
                "tool": "application",
                "action": "open",
                "target": "powershell"
            }

        # =====================================
        # File Manager
        # =====================================

        if re.search(r"(downloads)", command):
            return {
                "tool": "files",
                "action": "open",
                "target": "downloads"
            }

        if re.search(r"(documents)", command):
            return {
                "tool": "files",
                "action": "open",
                "target": "documents"
            }

        if re.search(r"(desktop)", command):
            return {
                "tool": "files",
                "action": "open",
                "target": "desktop"
            }

        # =====================================
        # Search
        # =====================================

        google = re.search(
            r"search (.+)",
            command
        )

        if google:
            return {
                "tool": "browser",
                "action": "google_search",
                "query": google.group(1)
            }

        youtube = re.search(
            r"search (.+) on youtube",
            command
        )

        if youtube:
            return {
                "tool": "browser",
                "action": "youtube_search",
                "query": youtube.group(1)
            }

        return {
            "tool": "llm"
        }


parser = IntentParser()


def parse(command: str):
    return parser.parse(command)