import pyautogui

# ----------------------------
# Single Keys
# ----------------------------

def enter():
    pyautogui.press("enter")

def space():
    pyautogui.press("space")

def tab():
    pyautogui.press("tab")

def esc():
    pyautogui.press("esc")

def backspace():
    pyautogui.press("backspace")

def delete():
    pyautogui.press("delete")

def insert():
    pyautogui.press("insert")

def home():
    pyautogui.press("home")

def end():
    pyautogui.press("end")

def page_up():
    pyautogui.press("pageup")

def page_down():
    pyautogui.press("pagedown")

# ----------------------------
# Arrow Keys
# ----------------------------

def up():
    pyautogui.press("up") 

def down():
    pyautogui.press("down")

def left():
    pyautogui.press("left")

def right():
    pyautogui.press("right")

# ----------------------------
# Function Keys
# ----------------------------

def f1(): pyautogui.press("f1")
def f2(): pyautogui.press("f2")
def f3(): pyautogui.press("f3")
def f4(): pyautogui.press("f4")
def f5(): pyautogui.press("f5")
def f6(): pyautogui.press("f6")
def f7(): pyautogui.press("f7")
def f8(): pyautogui.press("f8")
def f9(): pyautogui.press("f9")
def f10(): pyautogui.press("f10")
def f11(): pyautogui.press("f11")
def f12(): pyautogui.press("f12")

# ----------------------------
# CTRL Shortcuts
# ----------------------------

def select_all():
    pyautogui.hotkey("ctrl", "a")

def copy():
    pyautogui.hotkey("ctrl", "c")

def paste():
    pyautogui.hotkey("ctrl", "v")

def cut():
    pyautogui.hotkey("ctrl", "x")

def undo():
    pyautogui.hotkey("ctrl", "z")

def redo():
    pyautogui.hotkey("ctrl", "y")

def save():
    pyautogui.hotkey("ctrl", "s")

def open_file():
    pyautogui.hotkey("ctrl", "o")

def new_file():
    pyautogui.hotkey("ctrl", "n")

def print_file():
    pyautogui.hotkey("ctrl", "p")

def find():
    pyautogui.hotkey("ctrl", "f")

def replace():
    pyautogui.hotkey("ctrl", "h")

def refresh():
    pyautogui.hotkey("ctrl", "r")

def zoom_in():
    pyautogui.hotkey("ctrl", "+")

def zoom_out():
    pyautogui.hotkey("ctrl", "-")

def reset_zoom():
    pyautogui.hotkey("ctrl", "0")

# ----------------------------
# Browser
# ----------------------------

def new_tab():
    pyautogui.hotkey("ctrl", "t")

def close_tab():
    pyautogui.hotkey("ctrl", "w")

def reopen_tab():
    pyautogui.hotkey("ctrl", "shift", "t")

def next_tab():
    pyautogui.hotkey("ctrl", "tab")

def previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")

# ----------------------------
# Windows
# ----------------------------

def alt_tab():
    pyautogui.hotkey("alt", "tab")

def task_manager():
    pyautogui.hotkey("ctrl", "shift", "esc")

def lock_pc():
    pyautogui.hotkey("win", "l")

def run():
    pyautogui.hotkey("win", "r")

def explorer():
    pyautogui.hotkey("win", "e")

def settings():
    pyautogui.hotkey("win", "i")

def desktop():
    pyautogui.hotkey("win", "d")

def screenshot():
    pyautogui.hotkey("win", "shift", "s")

def emoji():
    pyautogui.hotkey("win", ".")

# ----------------------------
# Media
# ----------------------------

def play_pause():
    pyautogui.press("playpause")

def next_track():
    pyautogui.press("nexttrack")

def prev_track():
    pyautogui.press("prevtrack")

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")

def mute():
    pyautogui.press("volumemute")