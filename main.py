from globals import xPad, yPad

from io import FileIO
from progList import openNewWindow, openPrograms
from tkinter import Frame, font, ttk, filedialog
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, RIGHT, TOP, X, Y
import pyttsx3 as tts
import os
import tkinter as tk
from ttkbootstrap import Style


#
#   Text To Speech Configuration.
#
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
#
#
#

#
#  TkInter Init & Style.
#
style = Style(theme='journal')
root = style.master
root.title("PlanItOut")
root.geometry("500x350")

#
# Setup Frames Structures.
#
inputFrame = Frame(root)
inputFrame.pack(
    side=TOP, fill=BOTH, padx=16)

buttonFrame = Frame(root)
buttonFrame.pack(
    side=TOP, fill=BOTH, padx=16)

#
# Initialize few Variables.
#

varName = tk.StringVar(root)
varPath = tk.StringVar(root)


#
# Defined Few Functions.
#

def updatePaths():
    print("Updating paths")
    F = open("applications.txt", "a+")
    F.write(f'{varName.get()},{varPath.get()}\n')
    F.close()


def file_opener():
    input = filedialog.askopenfilename(
        filetypes=[("Applications", "*.exe")],)
    varPath.set(input)


def openPaths():
    for item in paths:
        tts.speak("Opening " + item)
        os.startfile(paths[item])


#
# DESIGN UI
#

ttk.Label(inputFrame, text='Enter Application Name',
          style='primary.TLabel').pack(pady=yPad, fill=X)
ttk.Entry(inputFrame, textvariable=varName).pack(pady=yPad, fill=X)

ttk.Label(inputFrame, text='Enter Application Path',
          style='primary.TLabel').pack(pady=yPad, fill=X)
ttk.Entry(inputFrame, textvariable=varPath).pack(pady=yPad, fill=X)

ttk.Button(inputFrame, text='Browse',
           command=file_opener).pack(side=LEFT, pady=yPad, fill=X, expand=1)

ttk.Separator(buttonFrame, orient=HORIZONTAL,
              style='primary.Horizontal.TSeparator').pack(pady=yPad, fill=X)

ttk.Button(buttonFrame, text='Add',
           command=updatePaths).pack(side=LEFT, padx=1, pady=yPad, fill=X, expand=1)

ttk.Button(buttonFrame, text='Open',
           command=lambda: openPrograms(root=root)).pack(side=LEFT, padx=1, pady=yPad, fill=X, expand=1)

ttk.Button(root, text='Show All Programs', style='primary.Outline.TButton',
           command=lambda: openNewWindow(root=root)).pack(side=BOTTOM, padx=xPad, fill=X, expand=1)

root.mainloop()
