import pyautogui
from core.voice import speak



def mute():

    pyautogui.press(
        "volumemute"
    )

    speak(
        "Muted"
    )



def volume_up():

    for i in range(10):

        pyautogui.press(
            "volumeup"
        )


def volume_down():

    for i in range(10):

        pyautogui.press(
            "volumedown"
        )