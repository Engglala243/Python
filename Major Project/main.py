import speech_recognition as sr
# import pyaudio
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

if __name__ == "__main__":
    speak("Initializing Parbhu...")
    while True:
        # Listen for the wake word "Devta"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Hello"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Parbhu always active tell me..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))
