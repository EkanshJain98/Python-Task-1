import os
import pyttsx3
import webbrowser
print("I can follow your instruction based on below commands")
print("1. Chrome")
print("2. VLC")
print("3. Notepad")
print("4. youtube")
print("5. whatsapp")
print("6. world's best website")
print("7. Facebook")
pyttsx3.speak("I can follow your instruction based on below commands.1. Chrome. 2. VLC. 3. Notepad. 4. youtube. 5. whatsapp. 6. world's best website. 7. Facebook")
while(True):
    a = input("Enter your command:- ")
    if("start" in a) and ("chrome" in a):
       pyttsx3.speak("opening Chrome browser for you")
       os.system("start chrome")
    elif("start" in a) and ("vlc" in a):
       pyttsx3.speak("opening VLC Player for you")
       os.system("start vlc")
    elif("start" in a) and ("notepad" in a):
       pyttsx3.speak("opening notepad for you")       
       os.system("start notepad")
    elif("start" in a)  and ("youtube" in a):
       pyttsx3.speak("opening youtube for you")
       webbrowser.open('http://youtube.com/')
    elif("start" in a)  and ("whatsapp" in a):
       pyttsx3.speak("opening whatsapp for you")
       webbrowser.open('https://web.whatsapp.com/')
    elif("start" in a) and ("best technology website" in a):
       pyttsx3.speak("opening world best technology webiste for you")
       webbrowser.open('https://technicalej.in/')
    elif("start" in a) and ("facebook" in a):
       pyttsx3.speak("opening facebook for you")
       webbrowser.open('https://www.facebook.com/ekansh.jain.395')   
    else:   
       break