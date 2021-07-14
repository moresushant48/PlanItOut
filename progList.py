import tkinter as tk
from tkinter import ttk


def openNewWindow(root):
    newWindow = tk.Toplevel(root)
    newWindow.title("All Programs")
    ttk.Label(newWindow,
              text="This is a new window").pack()
