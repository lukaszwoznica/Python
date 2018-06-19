from tkinter import *
import tkinter.font as tkF
import tkinter.filedialog as tkFD

def openFile():
    file_path = tkFD.askopenfilename()
    f = open(file_path, "r")
    textArea.delete("1.0", "end-1c")
    textArea.insert(END, f.read())

def saveFile():
    file_path = tkFD.asksaveasfilename()
    f = open(file_path, "w")
    f.write(textArea.get("1.0", "end-1c"))

def fontPlus():
    global font_size
    font_size += 1
    textArea.configure(font=("Helvetica", font_size))

def fontMinus():
    global font_size
    font_size -= 1
    textArea.configure(font=("Helvetica", font_size))


root = Tk()
root.title("Notepad")
font_size = 12

buttonsFrame = Frame(root)
textFrame = Frame(root)
buttonOpen = Button(buttonsFrame, text="Otwórz plik", command=openFile)
buttonSave = Button(buttonsFrame, text="Zapisz plik", command=saveFile)
buttonPlus = Button(buttonsFrame, text="Powiększ czcionkę", command=fontPlus)
buttonMinus = Button(buttonsFrame, text="Zmniejsz czcionkę", command=fontMinus)

scroll = Scrollbar(textFrame)
textArea = Text(textFrame, height=20, width=80, font=("Helvetica", font_size))
scroll.pack(side=RIGHT, fill=Y)
textArea.pack(side=LEFT, fill=Y)
scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set)


buttonsFrame.pack(side="top")
textFrame.pack(side="bottom")
buttonOpen.pack(side="left")
buttonSave.pack(side="left")
buttonPlus.pack(side="left")
buttonMinus.pack(side="left")

root.mainloop()
