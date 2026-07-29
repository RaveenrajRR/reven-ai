import os
from core.voice import speak


def shutdown():

    speak(
        "Shutdown"
    )

    os.system(
        "shutdown /s /t 5"
    )


def restart():

    speak(
        "Restart"
    )

    os.system(
        "shutdown /r /t 5"
    )


def lock():

    os.system(
    "rundll32.exe user32.dll,LockWorkStation"
    )

