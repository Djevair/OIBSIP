import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("Hello, I am your voice assistant")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "your name" in command:
        speak("I am a simple Python voice assistant")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
