import pyttsx3 ##pyttsx3 is a tool use to convert text to speech
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

alfred = pyttsx3.init()
voice= alfred.getProperty('voices')
alfred.setProperty('voice', voice[0].id) ## Male voice

def speak(audio):
    print('Alfred: ' + audio)
    alfred.say(audio)
    alfred.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p") #I is hour, M is min, p is AM or PM
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Morning Master Bruce.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir.")
    elif hour >= 18 and hour < 24:
        speak("Evening Master Bruce. You are back quite early.")
    else:
        speak("Hello Sir. I assume you just got back from patrolling")
    speak("Is there anything you need sir?")

def command():
    c = sr.Recognizer() ## Help receives voice input
    with sr.Microphone() as source:
        c.pause_threshould = 2 # Pause in 2s before listen 
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Bruce: " + query)
    except sr.UnknownValueError:
        print("I do not get what you are saying sir. Can you repeat or write it down for me please?")
        query = str(input('What I want to say is: '))
    return query

if __name__ =="__main__":
    welcome()
    while True:
        query = command().lower() #this is to take in lowercase command
        if "google" in query:
            speak("What do you want me to look up Master Bruce?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your what you asked for sir')
        if "youtube" in query:
            speak("What do you want me to look up Master Bruce?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your what you asked for sir')
        elif "open video" in query:
            url = f"https://www.youtube.com/watch?v=m-672F-VSSQ"
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("I'll see you later Master Bruce.") 
            quit()