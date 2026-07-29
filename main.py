from wakeword import wait_for_wakeword
from core.voice import listen
from core.command import execute
from core.assistant import activate_assistant, is_active

while True:

    if wait_for_wakeword():

        activate_assistant()

        while is_active():

            command = listen()

            if command:
                execute(command)
                