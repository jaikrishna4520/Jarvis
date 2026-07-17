import os


def open_downloads():
    os.startfile(os.path.expanduser("~/Downloads"))
    return "Opening Downloads."


def open_documents():
    os.startfile(os.path.expanduser("~/Documents"))
    return "Opening Documents."


def open_desktop():
    os.startfile(os.path.expanduser("~/Desktop"))
    return "Opening Desktop."