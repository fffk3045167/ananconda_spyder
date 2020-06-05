# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:33:52 2020

@author: Administrator
"""

from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print ('hi there, everyone!')

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below