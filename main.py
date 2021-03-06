from winBrowser import openBrowserWindow
from globals import APP_TXT, BR_TXT, TXT_SEPERATOR, alertBox, xPad, yPad, APP_NAME

import os
from io import FileIO
from winPrograms import openNewWindow
from tkinter import Frame, ttk, filedialog
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, TOP, X, Y
import tkinter as tk
from ttkbootstrap import Style


#
# Create files if dosen't exist.
#
try:
    open(APP_TXT, "r")
    open(BR_TXT, "r")
except:
    open(APP_TXT, "w+")
    open(BR_TXT, "w+")
    print("Created New TXTs.")

#
#  TkInter Init & Style.
#
style = Style(theme='journal')
root = style.master
root.title(APP_NAME)
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
    F = open(APP_TXT, "a+")
    if not varName.get() or not varPath.get():
        print("")
    else:
        F.write(f'{varName.get()}{TXT_SEPERATOR}{varPath.get()}\n')
        alertBox("Added " + varName.get() + " successfully.")
        varName.set("")  # clear App Name entry field
        varPath.set("")  # clear App Path entry field

    F.close()


def file_opener():
    input = filedialog.askopenfilename(
        filetypes=[("Applications", "*.exe")],)
    varPath.set(input)


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

ttk.Button(buttonFrame, text='Browser',
           command=lambda: openBrowserWindow(root=root)).pack(side=LEFT, padx=1, pady=yPad, fill=X, expand=1)

ttk.Button(root, text='Show All Programs', style='primary.Outline.TButton',
           command=lambda: openNewWindow(root=root)).pack(side=BOTTOM, padx=xPad, fill=X, expand=1)

root.mainloop()
