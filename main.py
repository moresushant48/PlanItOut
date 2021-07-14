from progList import openNewWindow
from tkinter import Frame, font, ttk
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, TOP, X, Y
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

paths = {}
xPad = 16
yPad = 8

#
#  TkInter Init & Style.
#
style = Style(theme='minty')
root = style.master
root.title("PlanItOut")
root.geometry("500x350")

main = Frame(root)
main.pack(
    side=TOP, fill=BOTH, padx=16, pady=16)

varName = tk.StringVar(root)
varPath = tk.StringVar(root)


def updatePaths():
    paths[varName.get()] = varPath.get()
    lstBox.delete(0, tk.END)
    for item in paths:
        lstBox.insert(tk.END, '{} : {}'.format(item, paths[item]))


def openPaths():
    for item in paths:
        tts.speak("Opening " + item)
        os.startfile(paths[item])


ttk.Label(main, text='Enter Application Name',
          style='primary.TLabel').pack(pady=yPad, fill=X)
ttk.Entry(main, textvariable=varName).pack(pady=yPad, fill=X)

ttk.Label(main, text='Enter Application Path',
          style='primary.TLabel').pack(pady=yPad, fill=X)
ttk.Entry(main, textvariable=varPath).pack(pady=yPad, fill=X)

ttk.Separator(main, orient=HORIZONTAL,
              style='primary.Horizontal.TSeparator').pack(pady=yPad, fill=X)

ttk.Button(main, text='Add',
           command=updatePaths).pack(side=LEFT, padx=1, pady=yPad, fill=X, expand=1)

ttk.Button(main, text='Open',
           command=openPaths).pack(side=LEFT, padx=1, pady=yPad, fill=X, expand=1)

ttk.Button(root, text='Show All Programs', style='primary.Outline.TButton',
           command=lambda: openNewWindow(root=root)).pack(side=BOTTOM, padx=xPad, fill=X, expand=1)

# lstBox = tk.Listbox(rightFrame)
# lstBox.pack(side=TOP)

# tts.speak("Hello Everyone, I am your assistant for today.")
# tts.speak("Lets Begin.")

root.mainloop()
