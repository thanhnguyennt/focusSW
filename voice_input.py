import speech_recognition as sr
import pyttsx3
import tkinter as tk

engine = pyttsx3.init()

def speak(text):
    engine.say(text)

def voice_command(welcome_instance, textfield):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language='en')

        textfield.delete(0, tk.END)  # Clear the current content
        textfield.insert(0, query)  # Insert the recognized query

        return query
    
    except sr.UnknownValueError:
        welcome_instance.say('Sorry, I did not catch that. Please repeat or type the name of the city.')
        query = ""

    return query
