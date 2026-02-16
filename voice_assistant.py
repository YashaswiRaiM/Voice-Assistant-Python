import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

def sptext():
    recognizer=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("cannot understand")
            
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
speechtx("hello welcome to voice assistant project")

if __name__  == '__main__':
    
    #if "hey siri" in sptext().lower():
    wake = sptext().lower()

    if "hey siri" in wake:
        speechtx("Yes, how can I help you?")
        print()

        while True:
            data1=sptext().lower()
            
            if "your name" in data1:
                name="my name is siri"
                speechtx(name)
                print()
            elif "old are you" in data1:
                age="i'm two year old"
                speechtx(age)
                print()
            elif "time" in data1:
                current_time=datetime.datetime.now().strftime("%I:%M %p")
                print("Current time:", current_time)
                print()
                speechtx("The time is " + current_time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
                print()
            elif "joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                print()
                speechtx(joke_1)
            
            elif "exit" in data1:
                print("-----------Thank You-------")
                print()
                speechtx("thank you")
                break
            
            time.sleep(2)
    else:
       print("Thanks ")
    
            
            
        