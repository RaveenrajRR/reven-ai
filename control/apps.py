import os
import psutil
from difflib import get_close_matches
from core.voice import speak

# -----------------------------
# Build Application Index
# -----------------------------
SEARCH_DIRS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expandvars(r"%LOCALAPPDATA%"),
]

APP_INDEX = {}


def build_app_index():
    APP_INDEX.clear()

    for folder in SEARCH_DIRS:
        if not os.path.exists(folder):
            continue

        for root, _, files in os.walk(folder):
            for file in files:

                if file.lower().endswith((".exe", ".lnk")):

                    name = os.path.splitext(file)[0].lower()

                    if "uninstall" in name:
                        continue

                    APP_INDEX[name] = os.path.join(root, file)


build_app_index()


# -----------------------------
# App Aliases
# -----------------------------
ALIASES = {
    "vs code": "visual studio code",
    "vscode": "visual studio code",
    "code": "visual studio code",
    "chrome": "google chrome",
    "edge": "microsoft edge",
    "word": "microsoft word",
    "excel": "microsoft excel",
    "ppt": "microsoft powerpoint",
    "paint": "paint",
    "calc": "calculator",
}


# -----------------------------
# Open App
# -----------------------------
def open_app(name):

    name = name.lower().strip()

    if name in ALIASES:
        name = ALIASES[name]

    # Exact Match
    if name in APP_INDEX:
        os.startfile(APP_INDEX[name])
        speak(f"Opening {name}")
        return

    # Partial Match
    for app in APP_INDEX:
        if name in app:
            os.startfile(APP_INDEX[app])
            speak(f"Opening {app}")
            return

    # Fuzzy Match
    match = get_close_matches(name, APP_INDEX.keys(), n=1, cutoff=0.6)

    if match:
        os.startfile(APP_INDEX[match[0]])
        speak(f"Opening {match[0]}")
        return

    speak("Application not found")


# -----------------------------
# Close App
# -----------------------------
def close_app(name):

    name = name.lower()

    found = False

    for process in psutil.process_iter(["pid", "name"]):

        try:

            process_name = process.info["name"].lower()

            if name in process_name:

                process.kill()

                speak(f"Closing {name}")

                found = True

                break

        except Exception:
            pass

    if not found:
        speak(f"{name} is not running")