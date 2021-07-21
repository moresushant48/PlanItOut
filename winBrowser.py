from tkinter import StringVar, ttk
from globals import BR_TXT, xPad, yPad
import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, END, TOP, X


def addItem(lstBox, varUrl):
    F = open(BR_TXT, "a+")
    if not varUrl.get():
        print("")
    else:
        F.write(f'{varUrl.get()}\n')
    F.close()
    loadItems(lstBox=lstBox)


def loadItems(lstBox):
    lstBox.delete(0, END)
    F = open(BR_TXT, "r+")
    lines = F.readlines()

    for line in lines:
        lstBox.insert(END, f"{line}")

    F.close()


def deleteItem(lstBox):
    for i in lstBox.curselection():
        with open(BR_TXT, "r") as f:
            lines = f.readlines()
        with open(BR_TXT, "w") as f:
            for line in lines:
                if line.find(lstBox.get(i)) != -1:
                    pass
                else:
                    f.write(line)
    loadItems(lstBox=lstBox)


def openBrowserWindow(root):
    newWindow = tk.Toplevel(root, padx=xPad, pady=yPad)
    newWindow.title("Web Browser")
    newWindow.geometry("400x400")

    varUrl = StringVar()

    ttk.Entry(newWindow, textvariable=varUrl).pack(side=TOP, fill=X)

    btnAdd = ttk.Button(newWindow, text="Add",
                        command=lambda: addItem(lstBox=lstBox, varUrl=varUrl))
    btnAdd.pack(side=TOP, fill=BOTH, pady=yPad)

    lstBox = tk.Listbox(
        newWindow)
    lstBox.pack(side=TOP, fill=BOTH)
    loadItems(lstBox=lstBox)

    btnDelete = ttk.Button(newWindow, text="Delete",
                           command=lambda: deleteItem(lstBox=lstBox))
    btnDelete.pack(side=TOP, fill=X, pady=yPad)
