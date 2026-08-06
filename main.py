from ui import show_listening_window
from wakeword import wait_for_wakeword
from core.voice import listen, speak
from core.command import execute
from core.assistant import activate_assistant, is_active
from control.type import main

while True:

    # Wait for wake word
    if wait_for_wakeword():

        activate_assistant()
        show_listening_window()

        # Assistant Loop
        while is_active():

            command = listen()

            if not command:
                continue

            response = execute(command)

            if response:
                speak(response)