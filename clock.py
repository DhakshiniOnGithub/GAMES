from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

def time():
    st = strftime('%H:%M:%S')
    label.config(text=st)
    label.after(1000, time)

label = Label(root, font = ("ds-digital", 80), background = "black", foreground = "hot pink")
label.pack(anchor='center')
time()

mainloop()
