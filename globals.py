from tkinter import messagebox
import webbrowser

APP_NAME = "Plan It Out"
APP_TXT = "applications.txt"
BR_TXT = "browser.txt"
TXT_SEPERATOR = " : "

paths = {}
xPad = 16
yPad = 8


def alertBox(msg):
    messagebox.showinfo(APP_NAME, msg)


def openWebBrowser(urls):
    for url in urls:
        webbrowser.open_new_tab(url=url)
