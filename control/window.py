import pyautogui

# Minimize Window
def minimize_window():
    pyautogui.hotkey("win", "down")

# Maximize Window
def maximize_window():
    pyautogui.hotkey("win", "up")

# Restore Window
def restore_window():
    pyautogui.hotkey("win", "down")

# Close Window
def close_window():
    pyautogui.hotkey("alt", "f4")

# Switch Window (Alt + Tab)
def switch_window():
    pyautogui.hotkey("alt", "tab")

# Next Window (same as Alt + Tab)
def next_window():
    pyautogui.hotkey("alt", "tab")



# Previous Window (Alt + Shift + Tab)
def previous_window():
    pyautogui.keyDown("alt")
    pyautogui.keyDown("shift")
    pyautogui.press("tab")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("alt")