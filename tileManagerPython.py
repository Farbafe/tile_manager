#!/usr/bin/python3

from Xlib import display
from tkinter import *
import sys


data = display.Display().screen().root.query_pointer()._data
original_x, original_y = data["root_x"], data["root_y"]


def returnValue(value):
#    window.destroy()
    sys.exit(value)

def key(event):
    sys.exit(int(event.char))

window = Tk()
window.geometry('+{}+{}'.format(original_x - 140, original_y - 70))
window.title("Select Position")
window.bind('<Key>', key)

btn = Button(window, text="Top Left", command=lambda: returnValue(1), pady=30, padx=30)
btn.grid(column=1, row=0)

btn = Button(window, text="Bottom Left", command=lambda: returnValue(0), pady=30, padx=20)
btn.grid(column=1, row=1)

btn = Button(window, text="Left", command=lambda: returnValue(4), pady=18, padx=20)
btn.grid(column=1, row=0, rowspan=2)

btn = Button(window, text="Center", command=lambda: returnValue(2), pady=72, padx=30)
btn.grid(column=2, row=0, rowspan=2)

btn = Button(window, text="Right", command=lambda: returnValue(3), pady=72, padx=30)
btn.grid(column=3, row=0, rowspan=2)

btn = Button(window, text="Center & Right", command=lambda: returnValue(5), pady=15, padx=5)
btn.grid(column=2, row=0, columnspan=2, rowspan=2)

btn = Button(window, text="Top", command=lambda: returnValue(9), pady=5, padx=90)
btn.grid(column=2, row=0, columnspan=2, sticky='n')

btn = Button(window, text="Bot", command=lambda: returnValue(6), pady=5, padx=90)
btn.grid(column=2, row=1, columnspan=2, sticky='s')

window.mainloop()
