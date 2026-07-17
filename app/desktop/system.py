import os


SAFE_MODE = True


def shutdown():

    if SAFE_MODE:
        return "Shutdown command received. SAFE MODE enabled."

    os.system("shutdown /s /t 1")
    return "Shutting down."


def restart():

    if SAFE_MODE:
        return "Restart command received. SAFE MODE enabled."

    os.system("shutdown /r /t 1")
    return "Restarting."


def lock():

    if SAFE_MODE:
        return "Lock command received. SAFE MODE enabled."

    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking computer."