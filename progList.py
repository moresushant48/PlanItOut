from globals import xPad, yPad

import os
import tkinter as tk
import pyttsx3 as tts
from tkinter import ttk
from tkinter.constants import BOTH, END, TOP


def openNewWindow(root):
    newWindow = tk.Toplevel(root)
    newWindow.title("All Programs")
    newWindow.geometry("400x300")

    F = open("applications.txt", "r+")
    lines = F.readlines()

    lstBox = tk.Listbox(newWindow)
    lstBox.pack(side=TOP, fill=BOTH, padx=xPad, pady=yPad)

    for line in lines:
        info = line.split(',')
        lstBox.insert(END, f"{info[0]} : {info[1]}")

    F.close()


def openPrograms(root):
    F = open("applications.txt", "r+")
    lines = F.readlines()
    for line in lines:
        info = line.split(',')
        tts.speak("Opening " + info[0])
        os.startfile(info[1][:-1])
