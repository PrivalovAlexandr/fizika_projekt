from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Чеш"/"Теория. Изотермический — CZ.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Чеш"/"Теория. Изобарный — CZ.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Чеш"/"Теория. Изохорный — CZ.pyw')

root = Tk()
root.title("Teorie")
root.geometry("700x200")
warn = Label(text = "Vyberte proces, kterým chcete doplnit své znalosti" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "Izotermický děj")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Izobarický děj")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Isochorický děj")
Task2.grid(row = 3, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )

display_button1.grid(row = 1, column = 4, sticky = "w")
display_button2.grid(row = 2, column = 4, sticky = "w")
display_button3.grid(row = 3, column = 4, sticky = "w")


root.mainloop()