#program that repeats after you.

import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
try:
    print("Recognizing...")    
    query = r.recognize_google(audio, language='en-in')
    print(f"Did you say: {query}")
    pyttsx3.speak(f"Did you say {query}")

except Exception as e:  
    print("Sorry didn't get you")  
    pyttsx3.speak("Sorry didn't get you")
