# coding=utf-8
__author__ = 'dimas'

from Tkinter import *
import grabber.GrabHtml
class But_print:

    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Печать"
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()

        self.text = Text(width=50, height=15, wrap=WORD)
        self.text.pack()


    def printer(self,event):
        self.text.delete(1.0,END)
        self.text.insert(END, grabber.GrabHtml.grab_quote())

root = Tk()
obj = But_print()
root.mainloop()