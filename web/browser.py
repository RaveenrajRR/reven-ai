import webbrowser
from core.voice import speak


def youtube():

    speak(
        "Opening Youtube"
    )

    webbrowser.open(
        "https://youtube.com"
    )



def google_search():

    speak(
        "Opening Google"
    )

    webbrowser.open(
        "https://google.com"
    )