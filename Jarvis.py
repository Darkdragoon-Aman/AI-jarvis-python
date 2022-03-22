#download all this module first

from ast import operator
import datetime
from posixpath import split
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit  # install flask module also
import speedtest

# -------------------------------------------------------------------------------------------------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("""
            ##     ############     ############    ##.       *##.   .##    ############
            ##     ##        ##     ##        @@     @@&     @@@     ,@@   .@@@.........
            ##     ## ###%&@ @@     @@ @@@@@@@@@      @@@  ,@@%      ,@@   .@@@@@@@@@@@@
            &@     @@.       @@     @@      %@@,       @@@ @@.       ,@@   ...........@@
  @@@@@@@@@@@@     @@.       @@     @@       .@@&       (@@.         ,@@    @@@@@@@@@@@@   
""")


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am Jarvis sir. please tell me how may i help you.")
    print("I am Jarvis sir. please tell me how may i help you.")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query


def takeCommandinput():
    query = input("user said: ")
    return query


com = takeCommand
run = True

# -------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    wishme()
    while run:
        query = com().lower()

        # Searching
        if 'hello jarvis' in query:
            print('Hello sir')
            speak('Hello sir')
        # search on wikipidea
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching...')
            query = query.replace("jarvis who is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        # search on google and youtube
        elif 'search' in query:
            speak('Searching on google...')
            query = query.replace("search on google", "")
            result = pywhatkit.search(query)
            speak("here is your result...")

        elif 'on youtube' in query:
            speak('Searching on youtube...')
            query = query.replace("play on youtube", "")
            result = pywhatkit.playonyt(query)
            speak("here is your result...")

        # Opening Sites
        elif 'open youtube' in query:
            webbrowser.Chrome(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("youtube.com")

        elif 'open gmail' in query:
            webbrowser.Chrome(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("gmail.com")

        elif 'open imdb' in query:
            webbrowser.Chrome(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("imdb.com")

        elif 'open amazon' in query:
            webbrowser.Chrome(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("amazon.in")

        # wheather
        elif 'weather' in query:
            webbrowser.Chrome(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("www.google.com/search?q=wheather")

        # What can you do?

        elif 'what can you do' in query:
            speak('I can do this all things')
            Command = """
__________________________________________________________________
1. talking with you.     (say: talking commands)
2. I can tell you jokes.
3. i can search any thing you whant on google,  wikipidea and yotube
4.I can show images of anything on internet.
5.i can test your internet speed.
6.tell the time and date.
7.open any Apps & Games Ex: Telegram, Zoom, Chrome and many more.
8.open any site Ex: youtube, gmail, imdb and many more.
9.close apps and sites.
10.i have inbuilt callculator
11.Roll Random Number.
12.play any music you have.
13.play any movie you have.
14.show you weather and tempreature of todays
15.stop your self.
__________________________________________________________________
"""
            print(Command)

        # music
        elif 'play music' in query:
            RN = random.randint(0, 3)
            music_dir = "C:\\Users\\admin\\Music\\myfavsongs"
            songs = os.listdir(music_dir)
            print(songs[RN])
            os.startfile(os.path.join(music_dir, songs[RN]))

        elif 'stop music' in query:
            os.system("taskkill /im Music.UI.exe /f")
            time.sleep(1)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        # open app

        elif 'open zoom' in query:
            codePath = "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk"
            os.startfile(codePath)

        elif 'close zoom' in query:
            os.system("taskkill /im zoom.exe /f")
            time.sleep(1)
            speak("i killed him")

        elif 'open telegram' in query:
            codePath = "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram.lnk"
            os.startfile(codePath)

        elif 'close telegram' in query:
            os.system("taskkill /im telegram.exe /f")
            time.sleep(1)
            speak("i killed him")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'close vs code' in query:
            os.system("taskkill /im code.exe /f")
            time.sleep(1)
            speak("i killed him")

        elif 'close chrome' in query:
            os.system("taskkill /im chrome.exe /f")
            time.sleep(1)
            speak("i killed him")

        elif 'stop jarvis' in query:
            run = False

        elif 'random number' in query:
            rand_i = random.randint(0, 9)
            outcomesNo = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            outcomeslastword = ["lololololol", "lmao", "opop", "xd", "xdxd", "sir can i concatenate with 9 please",
                                "leeleleleleel", "sir can i concatenate with 5 please", "kkk", ""]
            print(
                f"Sir, the random number is {outcomesNo[rand_i]} {outcomeslastword[rand_i]}")
            speak(
                f"Sir, the random number is {outcomesNo[rand_i]} {outcomeslastword[rand_i]}")

        # elif 'image of cat' in query:
        #     webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("https://source.unsplash.com/random/?cats")

        # elif 'image of dog' in query:
        #     webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab("https://source.unsplash.com/random/?dog")

        elif 'image of ' in query:
            speak(f"Finding the image on internet")
            query = query.replace("image of ", "")
            results = webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe").open_new_tab(
                f"https://source.unsplash.com/random/?{query}")
            speak(f"here is a image of {query}")

        # talking
        elif 'happy birthday' in query:
            ans = 'Happy birthday to you, happy birthday to you, happy birthday from Iron man, happy birthday to you. '
            print(ans)
            speak(ans)

        elif 'how are you' in query:
            ans = 'i am very very fine sir. how are you?'
            print(ans)
            speak(ans)

        elif 'fine' in query:
            ans = 'ok sir'
            print(ans)
            speak(ans)
        # whats the meaning of life
        elif 'meaning of life' in query:
            ans = "I have a factory warranty, so I don't worry about things like that."
            print(ans)
            speak(ans)
        # did you fart?
        elif 'fart' in query:
            ans = "I don't believe I did fart, no, but blame it on me if you want. Although they do say whoever smelled it dealt it."
            print(ans)
            speak(ans)
        # what am I thinking right now?
        elif 'thinking' in query:
            ans = "You're thinking if my Jarvis guesses what I'm thinking I'm going to freak out."
            print(ans)
            speak(ans)
        # self-destruct
        elif 'self destruct' in query:
            ans = "Self-destructing in 3, 2, 1... Actually I think I'll stick around."
            print(ans)
            speak(ans)
        # tell me your boss name
        elif 'boss' in query:
            ans = 'My boss name is Aman rai'
            print(ans)
            speak(ans)
        # let's party!
        elif "party" in query:
            ans = "I've been partying this whole time."
            print(ans)
            speak(ans)
        # can you rap?
        elif 'rap' in query:
            ans = "Hey you, so you want a rhyme. Here's what I can do, if you'll spare me the time. I can stick an appointment in your diary, and I'll attempt to answer your enquiry."
            print(ans)
            speak(ans)

        # Jarvis I'm your fan
        elif 'your fan' in query:
            ans = "ok that's cool but tell him don't come close to me"
            print(ans)
            speak(ans)
        
        # are you married?
        elif 'married' in query:
            ans = "I'm focusing on my career right now."
            print(ans)
            speak(ans)
        # do you have a girlfriend?
        elif 'girlfriend' in query:
            ans = "The only thing I'm really feeling a strong connection to is the Wi-Fi."
            print(ans)
            speak(ans)
        # where do babies come from
        elif 'babies come' in query:
            ans = 'It has to do with birds and bees, and, you see, when two people, ah. Actually, maybe your mum and dad know.'
            print(ans)
            speak(ans)
        # how old are you?
        elif 'how old' in query:
            ans = 'Old enough to know not to judge a book by its cover, but young enough to find the poo emoji funny.'
            print(ans)
            speak(ans)

        # talking command
        elif "talk" in query:
            ans = """
1. sing happy birthday for me
2. how are you?
3. whats the meaning od life
4. did you fart
5. what am i thinking write now?
6. jarvis self distruct yourself
7. tell me your boss name
8. lets party
9. can you rap
10. are you married
11. do you have girlfriend
12. where do babies come from
13. how old are you
            """
            print(ans)
            speak("This type of talk you can do with me.")

        # pLAY Movies
        elif 'play movie' in query:
            RM = random.randint(0, 1)
            movie_dir = "C:\\Users\\admin\\Videos\\Movies"
            movies = os.listdir(movie_dir)
            print(movies[RM])
            os.startfile(os.path.join(movie_dir, movies[RM]))

        elif 'close movie' in query:
            os.system(f"taskkill /im vlc.exe /f")
            time.sleep(1)

        # jokes

        elif "joke" in query:
            rand_i = random.randint(0, 9)
            outcomesjoke = [
                "I hear they’ve made a new artificially intelligent Oreo? It’s one smart cookie.",
                """A man creates the smartest AI and presents it to the UN, boasting it can solve any problem

“Oh yeah?” Said the president of the United States. “Ok, how do we solve poverty?”""",
                """Why are artificial intelligences in movies always female?

Because they’re never wrong.""",
                """My English teacher told us to write about the history of our life.

However, I hate writing, so I used AI to write it for me.

I guess you can say it’s an auto-biography. """,
                """Do you want to hear a construction joke?

Sorry, I’m still working on it.""",
                """Why should you never trust stairs?

They’re always up to something.""",
                """When does a joke become a ‘dad’ joke?

When it becomes apparent.""",
                """What does a house wear?

Address!""",
                """Why are toilets always so good at poker?

They always get a flush""",
                """How many tickles does it take to get an octopus to laugh?

Ten tickles"""]
            print(outcomesjoke[rand_i])
            speak(outcomesjoke[rand_i])

        # text and speak mode
        elif "text mode" in query:
            com = takeCommandinput
            speak("Text command activated")
            print("Text command activated")

        elif "audio mode" in query:
            com = takeCommand
            speak("audio command activated again...")
            print("audio command activated")

        #calculator
        elif "calculate" in query:      

            if com == takeCommand:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("what you want to calculate")
                    print("what you want to calculate (Example: 2 + 2)")
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    print("Recognizing...")
                    query = r.recognize_google(audio)
                    print(f"user said: {query}\n")

                    def add(x, y):
                        return x + y

                    def substrct(x, y):
                        return x - y

                    def multiply(x, y):
                        return x * y

                    def divide(x, y):
                        return x / y

                    if "+" in query:
                        splitnum = query.split()
                        numint = int(splitnum[0])
                        numint1 = int(splitnum[2])
                        ans = add(numint, numint1)
                        print(f"{numint} + {numint1} = {ans}")
                        speak(f"{numint} + {numint1} = {ans}")

                    if "plus" in query:
                        splitnum = query.split()
                        numint = int(splitnum[0])
                        numint1 = int(splitnum[2])
                        ans = add(numint, numint1)
                        print(f"{numint} + {numint1} = {ans}")
                        speak(f"{numint} + {numint1} = {ans}")

                    elif "-" in query:
                        splitnum = query.split()
                        numint = int(splitnum[0])
                        numint1 = int(splitnum[2])
                        ans = substrct(numint,numint1)
                        print(f"{numint} - {numint1} = {ans}")
                        speak(f"{numint} - {numint1} = {ans}")

                    elif "x" in query :
                        splitnum = query.split()
                        numint = int(splitnum[0])
                        numint1 = int(splitnum[2])
                        ans = multiply(numint,numint1)
                        print(f"{numint} * {numint1} = {ans}")
                        speak(f"{numint} * {numint1} = {ans}")

                    elif "multiply" in query :
                        splitnum = query.split()
                        numint = float(splitnum[0])
                        numint1 = float(splitnum[2])
                        ans = multiply(numint,numint1)
                        print(f"{numint} * {numint1} = {ans}")
                        speak(f"{numint} * {numint1} = {ans}")

                    elif "divide" in query:
                        splitnum = query.split()
                        numint = float(splitnum[0])
                        numint1 = float(splitnum[2]) 
                        ans = divide(numint,numint1)
                        print(f"{numint} / {numint1} = {ans}")
                        speak(f"{numint} divide {numint1} = {ans}")

                    elif "/" in query:
                        splitnum = query.split()
                        numint = float(splitnum[0])
                        numint1 = float(splitnum[2]) 
                        ans = divide(numint,numint1)
                        print(f"{numint} / {numint1} = {ans}")
                        speak(f"{numint} divide {numint1} = {ans}")
            else:
                def add(x, y):
                    return x + y

                def substrct(x, y):
                    return x - y

                def multiply(x, y):
                    return x * y

                def divide(x, y):
                    return x / y

                print("Calulator")
                print("1.add")
                print("2.substrct")
                print("3.multiply")
                print("4.divide")

                while True:
                    Num1 = float(input("Enter ur first number:"))
                    Num2 = float(input("Enter ur second number:"))

                    choice = input("Enter ur Choise(1/2/3/4): ")
                    if choice == "1":
                        print(Num1, "+", Num2, "=", add(Num1, Num2))

                    elif choice == "2":
                        print(Num1, "-", Num2, "=", substrct(Num1, Num2))

                    elif choice == "3":
                        print(Num1, "*", Num2, "=", multiply(Num1, Num2))

                    elif choice == "4":
                        print(Num1, "/", Num2, "=", divide(Num1, Num2))

                    else:
                        print("fuck off")

                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                        break
        
        #speed test
        elif "speed test" in query:
            speak("Please wait... i am Processing your speed test")
            print("Pls wait... i am Processing your speed test")
            speedtester = speedtest.Speedtest()
            ping = speedtester.results.ping
            download = speedtester.download()
            upload = speedtester.upload()
            download_mbs = round(download / (10**6), 2)
            upload_mbs = round(upload / (10**6), 2)
            print(f"Your ping is {ping}, your download speed is {download_mbs}mbps and your upload speed is {upload_mbs}mbps")
            speak(f"Your ping is {ping}, your download speed is {download_mbs}mbps and your upload speed is {upload_mbs}mbps")