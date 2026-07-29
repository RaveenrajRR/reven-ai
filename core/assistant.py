import sys

assistant_active = False   # ஆரம்பத்தில் wake word-க்காக wait பண்ணும்

def activate_assistant():
    global assistant_active
    assistant_active = True

def deactivate_assistant():
    global assistant_active
    assistant_active = False

def sleep_mode():
    global assistant_active
    assistant_active = False

def wake_up():
    global assistant_active
    assistant_active = True

def is_active():
    return assistant_active

def exit_assistant():
    sys.exit()