"""
JARVIS Command Router
Enterprise Version - Phase 3.3
"""

import re

from app.desktop import applications
from app.desktop import browser
from app.desktop import files
from app.desktop import system


class CommandRouter:

    def __init__(self):

        self.routes = [

            # ==================================================
            # Browser
            # ==================================================

            (r".*\b(open|launch|start).*(chrome|browser)\b.*",
             browser.open_chrome),

            (r".*\b(incognito|private browsing|private mode)\b.*",
             browser.open_incognito),

            (r".*\b(open).*(youtube)\b.*",
             browser.open_youtube),

            (r".*\b(open).*(gmail)\b.*",
             browser.open_gmail),

            (r".*\b(open).*(chatgpt)\b.*",
             browser.open_chatgpt),

            (r".*\b(open).*(github)\b.*",
             browser.open_github),

            (r".*\b(open).*(linkedin)\b.*",
             browser.open_linkedin),

            (r".*\b(open).*(stack ?overflow)\b.*",
             browser.open_stackoverflow),

            (r".*\b(open).*(aws console)\b.*",
             browser.open_aws_console),

            # ==================================================
            # Desktop Applications
            # ==================================================

            (r".*\b(vs code|visual studio code|code)\b.*",
             applications.open_vscode),

            (r".*\b(notepad)\b.*",
             applications.open_notepad),

            (r".*\b(calculator|calc)\b.*",
             applications.open_calculator),

            (r".*\b(paint)\b.*",
             applications.open_paint),

            (r".*\b(command prompt|cmd)\b.*",
             applications.open_cmd),

            (r".*\b(powershell|power shell)\b.*",
             applications.open_powershell),

            (r".*\b(file explorer|explorer)\b.*",
             applications.open_explorer),

            (r".*\b(task manager)\b.*",
             applications.open_task_manager),

            # ==================================================
            # Files
            # ==================================================

            (r".*\b(downloads)\b.*",
             files.open_downloads),

            (r".*\b(documents)\b.*",
             files.open_documents),

            (r".*\b(desktop)\b.*",
             files.open_desktop),

            # ==================================================
            # System
            # ==================================================

            (r".*\b(lock)\b.*",
             system.lock),

            (r".*\b(restart)\b.*",
             system.restart),

            (r".*\b(shutdown computer)\b.*",
             system.shutdown)

        ]

    def execute(self, command: str):

        command = command.lower().strip()

        # ------------------------------
        # Dynamic Google Search
        # ------------------------------

        google_match = re.search(
            r"search (.+?) on google",
            command
        )

        if google_match:

            return browser.google_search(
                google_match.group(1)
            )

        google_match = re.search(
            r"search (.+)",
            command
        )

        if google_match:

            return browser.google_search(
                google_match.group(1)
            )

        # ------------------------------
        # Dynamic YouTube Search
        # ------------------------------

        youtube_match = re.search(
            r"search (.+?) on youtube",
            command
        )

        if youtube_match:

            return browser.youtube_search(
                youtube_match.group(1)
            )

        # ------------------------------
        # Static Commands
        # ------------------------------

        for pattern, function in self.routes:

            if re.search(pattern, command):

                return function()

        return None


router = CommandRouter()


def route(command: str):
    return router.execute(command)