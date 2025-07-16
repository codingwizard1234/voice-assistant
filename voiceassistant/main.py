import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from youtube import *
from spotify import *
import randfacts
from jokes import *
import datetime


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak (text):
    engine.say(text)
    engine.runAndWait()

print("Hello!! My name is Zee. "
      "I'm your voice assistant. "
      "How are you?")
speak("Hello!! My name is Zee. "
      "I'm your voice assistant. "
      "How are you?")


r = sr.Recognizer()
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    print("I am also having a good day.")
    speak("I am also having a good day.")
print("What can I do for you?")
speak("what can I do for you?")

with sr.Microphone () as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise (source,1.2)
    print("listening...")
    audio = r.listen (source)
    text2 = r.recognize_google (audio)

if "information" in text2:
    print("You need information related to which topic?")
    speak("you need information related to which topic?")

    with sr.Microphone () as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise (source,1.2)
        print("listening...")
        audio = r.listen (source)
        infor = r.recognize_google (audio)

        class infow():
            def __init__(self):
                self.driver = webdriver.Chrome (executable_path='C:\Windows\chromedriver-win32\chromedriver.exe')

            def get_info(self, query):
                self.query = query
                self.driver.get(url="https://www.wikipedia.org")
                search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
                search.click()
                search.send_keys(query)
                enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
                enter.click()

        print("opening wikipedia")
        speak("opening wikipedia")
        assist1 = infow()
        assist1.get_info(infor)

elif "play" and "video" in text2:
    print(text2)
    print("Which video you want to watch?")
    speak("Which video you want to watch?")

    with sr.Microphone () as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise (source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("opening youtube")
    speak("opening youtube")

    assist = youtube()
    assist.play(vid)

elif "listen" and "music" in text2:
    print(text2)
    print("opening spotify")
    speak("opening spotify")

    assist = music()
    assist.play(" ")


elif "fact" in text2:
    print(text2)
    x=randfacts.get_fact()
    print("did you know that, ",x)
    speak("did you know that, " + x)


elif "joke" in text2:
    print(text2)
    print("Sure, get ready for some chuckles")
    speak("sure, get ready for some chuckles")
    ar=joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])

elif "time" and "date" in text2:
    print(text2)
    today_date = datetime.datetime.now()
    speak("Today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") + "And its currently"
          + today_date.strftime("%I") + today_date.strftime("%M") + today_date.strftime("%p"))

else:
    speak("Speak something dont be shy")




