from globals import APP_TXT, xPad, yPad, TXT_SEPERATOR

import os
import tkinter as tk
import pyttsx3 as tts
from tkinter import ttk
from tkinter.constants import BOTH, END, TOP, X


def loadApplicationsToListbox(lstBox):
    lstBox.delete(0, END)
    F = open(APP_TXT, "r")
    lines = F.readlines()

    for line in lines:
        info = line.split(TXT_SEPERATOR)
        lstBox.insert(END, f"{info[0]}{TXT_SEPERATOR}{info[1]}")

    F.close()


def deleteItem(lstBox):
    for i in lstBox.curselection():
        with open(APP_TXT, "r") as f:
            lines = f.readlines()
        with open(APP_TXT, "w") as f:
            for line in lines:
                if line.find(lstBox.get(i)) != -1:
                    pass
                else:
                    f.write(line)
    loadApplicationsToListbox(lstBox=lstBox)


def openNewWindow(root):
    newWindow = tk.Toplevel(root, padx=xPad, pady=yPad)
    newWindow.title("All Programs")
    newWindow.geometry("400x300")

    lstBox = tk.Listbox(
        newWindow)
    lstBox.pack(side=TOP, fill=BOTH)
    btnDelete = ttk.Button(newWindow, text="Delete",
                           command=lambda: deleteItem(lstBox=lstBox))
    btnDelete.pack(fill=X)
    loadApplicationsToListbox(lstBox=lstBox)
