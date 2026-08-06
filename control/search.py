import webbrowser
import urllib.parse
from core.voice import speak


def search_google(query):
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(url)


def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    webbrowser.open(url)


def search_wikipedia(query):
    url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(query)}"
    webbrowser.open(url)


def search_images(query):
    url = f"https://www.google.com/search?tbm=isch&q={urllib.parse.quote(query)}"
    webbrowser.open(url)


def open_chatgpt():
    webbrowser.open("https://chat.openai.com/")

