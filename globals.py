from tkinter import messagebox
from shutil import copyfile
import os
from shutil import copy2

USERAPPDATA_PATH = "C:\\Users\\" + os.getlogin() + \
    "\\AppData\\Roaming\\PlanItOut\\"

APP_NAME = "Plan It Out"
APP_TXT = USERAPPDATA_PATH + "applications.txt"
BR_TXT = USERAPPDATA_PATH + "browser.txt"
TXT_SEPERATOR = " : "

paths = {}
xPad = 16
yPad = 8


def alertBox(msg):
    messagebox.showinfo(APP_NAME, msg)
