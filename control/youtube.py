import pyautogui

def playpause():
    print("play/pause")
    pyautogui.press("k")

def fullscreen():
    pyautogui.press("f")

def mute():
    pyautogui.press("m")

def volume_up():
    pyautogui.press("up")

def volume_down():
    pyautogui.press("down")

def forward():
    pyautogui.press("l")

def backward():
    pyautogui.press("j")

def next_video():
    pyautogui.hotkey("shift", "n")

def captions():
    pyautogui.press("c")

def theater_mode():
    pyautogui.press("t")