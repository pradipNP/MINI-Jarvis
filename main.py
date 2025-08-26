import speech_recognition as sr
import webbrowser
import pyttsx3  # Text to speech
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split()[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        try:
            print("recognizing...")
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                print("Wake word detected. jarvis active...")
                
                # 🔹 Speak after closing mic session
                speak("Ya")

                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
