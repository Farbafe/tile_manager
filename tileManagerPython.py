#!/usr/bin/python3

from tkinter import *
import sys


def returnValue(value):
#    window.destroy()
    sys.exit(value)

def key(event):
    sys.exit(int(event.char))

window = Tk()
 
window.title("Select Position")
window.bind('<Key>', key)

btn = Button(window, text="Top Left", command=lambda: returnValue(1))
btn.grid(column=1, row=0)

btn = Button(window, text="Bottom Left", command=lambda: returnValue(0))
btn.grid(column=1, row=1)

btn = Button(window, text="Center", command=lambda: returnValue(2))
btn.grid(column=2, row=0)

btn = Button(window, text="Right", command=lambda: returnValue(3))
btn.grid(column=3, row=0)

btn = Button(window, text="Center & Right", command=lambda: returnValue(5))
btn.grid(column=2, row=1, columnspan=2)
 
window.mainloop()
