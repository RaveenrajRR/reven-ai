import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()

engine.setProperty(
    "rate",
    170
)


def speak(text):

    print("AI:",text)

    engine.say(text)
    engine.runAndWait()



recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            phrase_time_limit=8
        )


    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:",text)

        return text.lower()


    except:

        return ""