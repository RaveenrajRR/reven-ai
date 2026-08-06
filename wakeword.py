from core.voice import listen, speak
from ui import show_listening_window   # UI function

WAKE_WORD = "activate"


def wait_for_wakeword():
    while True:
        command = listen().lower()

        if not command:
            continue

        if WAKE_WORD in command:
            show_listening_window()
            speak("Yes, I am listening")     # Center window open
            print("Wake word detected!")
            return True