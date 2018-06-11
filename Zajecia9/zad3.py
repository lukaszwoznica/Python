from tkinter import *
import tkinter.messagebox as tkMsgBox
import tkinter.font as tkFont

root = Tk()


def add():
    l1 = int(entryL1.get())
    l2 = int(entryL2.get())
    result = l1 + l2
    entryResult.configure(state='normal')
    entryResult.delete(0, END)
    entryResult.insert(END, str(result))
    entryResult.configure(state='readonly')


def sub():
    l1 = int(entryL1.get())
    l2 = int(entryL2.get())
    result = l1 - l2
    entryResult.configure(state='normal')
    entryResult.delete(0, END)
    entryResult.insert(END, str(result))
    entryResult.configure(state='readonly')


def mul():
    l1 = int(entryL1.get())
    l2 = int(entryL2.get())
    result = l1 * l2
    entryResult.configure(state='normal')
    entryResult.delete(0, END)
    entryResult.insert(END, str(result))
    entryResult.configure(state='readonly')


def div():
    l1 = int(entryL1.get())
    l2 = int(entryL2.get())
    try:
        result = l1 / l2
    except ZeroDivisionError:
        tkMsgBox.showinfo("Błąd", "Nie można dzielić przez 0!")
        return
    entryResult.configure(state='normal')
    entryResult.delete(0, END)
    entryResult.insert(END, str(result))
    entryResult.configure(state='readonly')


default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size="13")
root.option_add("*Font", default_font)

frameTop = Frame(root)
frameBottom = Frame(root, pady="5")
labelL1 = Label(frameTop, text="Liczba 1: ")
labelL2 = Label(frameTop, text="Liczba 2: ")
labelResult = Label(frameTop, text="Wynik: ")
entryL1 = Entry(frameTop, width="10", justify="center")
entryL2 = Entry(frameTop, width="10", justify="center")
entryResult = Entry(frameTop, width="10", justify="center", state="readonly")
buttonSum = Button(frameBottom, text="+", width="4", command=add)
buttonSub = Button(frameBottom, text="-", width="4", command=sub)
buttonMul = Button(frameBottom, text="*", width="4", command=mul)
buttonDiv = Button(frameBottom, text="/", width="4", command=div)

frameTop.grid()
labelL1.grid(row="0", column="0")
entryL1.grid(row="0", column="1")
labelL2.grid(row="1", column="0")
entryL2.grid(row="1", column="1")
labelResult.grid(row="2", column="0")
entryResult.grid(row="2", column="1")
frameBottom.grid()
buttonSum.grid(row="0", column="0")
buttonSub.grid(row="0", column="1")
buttonMul.grid(row="0", column="3")
buttonDiv.grid(row="0", column="4")

root.mainloop()
