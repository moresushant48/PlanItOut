from tkinter import messagebox

APP_NAME = "Plan It Out"
APP_TXT = "applications.txt"
TXT_SEPERATOR = " : "

paths = {}
xPad = 16
yPad = 8


def alertBox(msg):
    messagebox.showinfo(APP_NAME, msg)
