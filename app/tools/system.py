import os


def shutdown():
    os.system("shutdown /s /t 1")
    return "Shutting down computer."


def restart():
    os.system("shutdown /r /t 1")
    return "Restarting computer."


def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking computer."