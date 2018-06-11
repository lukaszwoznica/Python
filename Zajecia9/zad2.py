from tkinter import *
import tkinter.messagebox as tkMsgBox
import tkinter.font as tkFont

root = Tk()


def countdown(time):
    labelTime.configure(text=time)

    if time > 0:
        root.after(1000, countdown, time - 1)
    else:
        tkMsgBox.showinfo("Uwaga!", "Zakończono odliczanie")


def start():
    x = int(entry1.get())
    countdown(x)

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size="13")
root.option_add("*Font", default_font)


labelTime = Label(root, text="Czekam")
labelEntry = Label(root, text="Podaj liczbe sekund: ")
entry1 = Entry(root, width="10", justify="center", text="5")
button = Button(root, text="Start", width="15", command=start)

labelTime.grid(row="0", column="0", columnspan="2")
labelEntry.grid(row="1", column="0")
entry1.grid(row="1", column="1")
button.grid(row="2", column="0", columnspan="2")

root.mainloop()
