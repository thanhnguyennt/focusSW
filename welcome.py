import pyttsx3
import datetime

def init_assistance():
    assistance = pyttsx3.init()
    voices = assistance.getProperty('voices')
    assistance.setProperty('voice', voices[1].id)
    return assistance

def speak(assistance, audio=None):
    assistance.say(audio)
    assistance.runAndWait()

def get_time():
    return datetime.datetime.now().strftime('%I:%M:%p')

def welcome(assistance):
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak(assistance, 'Good morning sir')
    elif 12 <= hour < 18:
        speak(assistance, 'Good afternoon sir')
    else:
        speak(assistance, 'Good night sir')
    speak(assistance, 'How would you like to check the weather?')