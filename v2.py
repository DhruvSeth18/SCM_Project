from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import openai
import pywhatkit as pwt


root=Tk()
root.geometry("600x400+600+200")
root.configure(bg="#C9EEFF")
root.title("VOICE ASSISTANT with GPT")
f1=Frame(root,height=100,bg='yellow').pack(fill='x')
li=Label(f1,text="VOICE ASSISTANT",font =('Arial',30,'bold'),bg="yellow").place(x=75,y=25)
os.environ["OPENAI_API_KEY"] = "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"
# Retrieve the API key from the secret manager
openai.api_key = os.environ["OPENAI_API_KEY"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0])
engine.setProperty('rate',185)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    time = int(datetime.datetime.now().hour)
    if time<=12:
        speak("Goodmorning Sir ")
    elif 12<time<=18:
        speak("Good Afternoon Sir")
    elif 18<time<=24:
        speak("Good Evening Sir")
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        my_label.config(text="Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            my_label.config(text="recognising...")
            query =r.recognize_google(audio,language="en-in")
        except Exception as e:
            print(e)
            speak("can't hear")
            return "None"
    return query
def Listen():
    global root
    greet()
    while 1:
        query = take().lower()
        print(query)
        if 'rohit' in query:
            query = query.replace("rohit", "")
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": query}])
            text = response.choices[0].message.content
            speak(text)
            print(query)

        elif 'hello' in query:
            speak("Hello Sir what can i do for you ")
            print(query)

        elif 'what is my name' in query:
            speak("Sir your name is Dhruv Seth")
            print(query)

        elif 'play' in query:
            query=query.replace("play","")
            loc=f"C:\\Users\\yootu\\Downloads\\song\\{query}.mp3"
            loc=loc.replace(" ","")
            os.startfile(loc)

        elif 'on youtube' in query:
            query=query.replace("on youtube","")
            pwt.playonyt(query)

        elif 'open google' in query:
            webbrowser.open("google.com")
            print(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print(query)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            print(query)

        elif 'wikipedia' in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ...")
            speak(results)
            print(results)

        elif "meaning" in query:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": query}])
            text = response.choices[0].message.content
            speak(text)
            print(text)

        elif 'nothing' in query:
            speak("ok sir if you need me just ask ")

        elif 'good morning' in query:
            speak("good morning sir! How may i help u.")

        elif 'good afternoon' in query:
            speak("good afternoon sir! How is your day going.")

        elif 'good evening' in query:
            speak("good evening sir! How is your day going.")

        elif 'good night' in query:
            speak("Good night sir! how was your day spent?")

        elif ('shutdown' in query) or ('stop listen' in query) or ("don't listen" in query):
            speak("Ok sir")
            root.destroy()
            break

round = PhotoImage(file="BUTTON.png")
B1=Button(root,image=round,bg="#C9EEFF",border=0,command=Listen).place(x=280,y=195)
my_label=Label(root,text="",bg="#C9EEFF")
my_label.place(x=220,y=260)
root.mainloop()