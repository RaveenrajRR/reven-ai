import os
from datetime import datetime
import pyautogui
from core.voice import speak


def screenshot():
    try:
        # Pictures folder
        pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")

        # Create filename with date and time
        filename = f"K_AI_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(pictures_folder, filename)

        # Take screenshot
        image = pyautogui.screenshot()
        image.save(filepath)

        speak("Screenshot captured successfully.")

        print(f"Screenshot saved: {filepath}")

        return filepath

    except Exception as e:
        print(f"Screenshot Error: {e}")
        speak("Sorry, I could not capture the screenshot.")
        return None