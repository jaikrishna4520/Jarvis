import os
import subprocess
import shutil


def _open_application(command, app_name):
    """
    Opens an application using subprocess.
    """

    try:
        subprocess.Popen(command)
        return f"Opening {app_name}."

    except FileNotFoundError:
        return f"{app_name} is not installed."

    except Exception as e:
        return f"Failed to open {app_name}: {e}"


def open_vscode():
    """
    Open Visual Studio Code.
    """

    code_path = shutil.which("code")

    if code_path:
        return _open_application([code_path], "Visual Studio Code")

    possible_paths = [
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
        )
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return _open_application([path], "Visual Studio Code")

    return "Visual Studio Code is not installed."


def open_notepad():
    return _open_application(["notepad.exe"], "Notepad")


def open_calculator():
    return _open_application(["calc.exe"], "Calculator")


def open_paint():
    return _open_application(["mspaint.exe"], "Paint")


def open_cmd():
    return _open_application(["cmd.exe"], "Command Prompt")


def open_powershell():
    return _open_application(["powershell.exe"], "PowerShell")


def open_explorer():
    return _open_application(["explorer.exe"], "File Explorer")


def open_task_manager():
    return _open_application(["taskmgr.exe"], "Task Manager")