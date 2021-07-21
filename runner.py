from globals import APP_TXT, BR_TXT, TXT_SEPERATOR
import pyttsx3 as tts
import os
import webbrowser

#
#   Text To Speech Configuration.
#


def setupTTS():
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()
#
#
#


def openPrograms():
    setupTTS()
    F = open(APP_TXT, "r+")
    lines = F.readlines()
    for line in lines:
        info = line.split(TXT_SEPERATOR)
        tts.speak("Opening " + info[0])
        os.startfile(info[1][:-1])


def openUrlsInBrowser():
    F = open(BR_TXT, "r")
    lines = F.readlines()

    for line in lines:
        webbrowser.open_new_tab(line)

    F.close()


openPrograms()
openUrlsInBrowser()
