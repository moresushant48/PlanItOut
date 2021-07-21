from tkinter import messagebox
from shutil import copyfile
import os
from shutil import copy2

STARTUP_PATH = "C:\\Users\\" + os.getlogin() + \
    "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
START_PATH = "C:\\Users\\" + os.getlogin() + \
    "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\start.bat"
APP_NAME = "Plan It Out"
APP_TXT = "applications.txt"
BR_TXT = "browser.txt"
TXT_SEPERATOR = " : "

paths = {}
xPad = 16
yPad = 8


def copyStartBatch():
    if(not os.path.exists(START_PATH)):
        try:
            print(copy2("start.bat", STARTUP_PATH))
        except Exception as e:
            print("Copy error : " + e)


def alertBox(msg):
    messagebox.showinfo(APP_NAME, msg)
