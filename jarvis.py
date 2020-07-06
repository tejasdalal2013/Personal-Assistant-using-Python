
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb 
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time Is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current Date Is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    rate = engine.getProperty('rate')   
    print (rate)                        
    engine.setProperty('rate', 170)  
    volume = engine.getProperty('volume')   
    print (volume)                          
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[1].id) 
    speak("Welcome Back Sir")

    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir")
    elif hour >=18 and hour<24:
        speak("Good Evening Sir")
    else:
        speak("Good nigth sir")
    speak("Jarvis At Your Service Please Tell Me how Can i Help You")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio ,language= 'en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say It Again Please")

        return "None"

    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mpmodi985@gmail.com', 'Maheshmodi0987')
    server.sendmail('mpmodi985@gmail.com', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\User\\Documents\\Jarvis\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())





if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What Should I Say??")
                content = takeCommand()
                to = 'tejasdalal2013@gmail.com'
                sendEmail(to, content)
                speak("Email has been Sent Sucess")
            except Exception as e:
                print(e)
                speak("Unable to send email try again Later")
        elif 'search on chrome' in query:
            speak("What Should I Search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said to remember that" +remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()







        elif 'offline' in query:
            quit()

