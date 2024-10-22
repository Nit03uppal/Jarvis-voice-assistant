import speech_recognition as sr
import webbrowser
import pyttsx3#for text to speech
import music_library
import time
from datetime import datetime
import os
import pyjokes

#open custom applications
def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad.exe")
    elif "calculator" in app_name:
        os.system("calc.exe")
    else:
        speak("Sorry, I don't know how to open that application.")


#set alarms
def set_alarm(alarm_time):
    current_time = datetime.now().strftime("%H:%M")
    while current_time != alarm_time:
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(10)
    speak("Wake up! It's time!")


#google search

def google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    speak(f"Here are the results for {query}")

#tell jokes

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)


#check date and time
def get_time():
    current_time = datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")

def get_date():
    current_date = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


#exit command
def exit_jarvis():
    speak("Goodbye!")
    exit()


#pip install pocketsphinx

recognizer=sr.Recognizer()
engine=pyttsx3.init() #initializing pyttsx3 engine


#takes text as input and speaks that 
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        #song=c.lower().split(" ")[1:]
        song = " ".join(c.lower().split()[1:])
        song=song.lower()
        link=music_library.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")

    elif "tell me a joke" in c.lower():
        tell_joke()
    
    elif "search" in c.lower():
        query = c.lower().split("search")[-1].strip()
        google_search(query)

    elif "set alarm" in c.lower():
        alarm_time = c.lower().split("for")[-1].strip()
        speak(f"Setting alarm for {alarm_time}")
        set_alarm(alarm_time)

    elif "open" in c.lower():
        app_name = c.lower().split("open")[-1].strip()
        speak(f"opening {app_name}")
        open_application(app_name)

    elif "time" in c.lower():
        get_time()
    elif "date" in c.lower():
        get_date()


    elif "exit" in c.lower() or "bye" in c.lower():
        exit_jarvis()
    


if __name__=="__main__":
    speak("Hello How may I help you")
    #speak("To initiate the interaction please speak Jarvis and then speak the instructions")
    while True:
        #listen for the wake word Morgis to start the interaction

        #obtain audio from the microphone
        r=sr.Recognizer()
    

        print("Recognizing")

        #recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Speak Now")
                audio=r.listen(source,timeout=5,phrase_time_limit=5)
            word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes...")
                #listen foword
                with sr.Microphone() as source:
                    print("Listening Now....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
    
        except Exception as e:
            print("Error;{0}".format(e))

