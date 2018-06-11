from tkinter import *
import tkinter.messagebox
import  tkinter.font as tkFont

def changeColor(v):
    if v.get() == 1:
        button.config(fg="red")
    elif v.get() == 2:
        button.config(fg="green")
    elif v.get() == 3:
        button.config(fg="blue")


def showMsgBox():
    tkinter.messagebox.showinfo("Komunikat", "Kliknięto przycisk!")


root = Tk()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size="13")
root.option_add("*Font", default_font)


frameTop = Frame(root)
frameBottom = Frame(root)
v = IntVar()
radio1 = Radiobutton(frameTop, text="Czerwony", variable=v, value=1, command=lambda: changeColor(v))
radio2 = Radiobutton(frameTop, text="Zielony", variable=v, value=2, command=lambda: changeColor(v))
radio3 = Radiobutton(frameTop, text="Niebieski", variable=v, value=3, command=lambda: changeColor(v))
button = Button(frameBottom, text="Zmien kolor", command=showMsgBox)

frameTop.pack()
frameBottom.pack(side=BOTTOM)
radio1.pack(side=LEFT)
radio2.pack(side=LEFT)
radio3.pack(side=LEFT)
button.pack(side=BOTTOM)

root.mainloop()
