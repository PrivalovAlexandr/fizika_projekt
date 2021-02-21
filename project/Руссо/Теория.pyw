from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Руссо"/"Теория. Изотермический.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Руссо"/"Теория. Изобарный.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Руссо"/"Теория. Изохорный.pyw')

root = Tk()
root.title("Меню")
root.geometry("700x200")
warn = Label(text = "Выберите процесс по которому вы хотите пополнить свои знания" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "Изотермический процесс")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Изобарный процесс")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Изохорный процесс")
Task2.grid(row = 3, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )

display_button1.grid(row = 1, column = 4, sticky = "w")
display_button2.grid(row = 2, column = 4, sticky = "w")
display_button3.grid(row = 3, column = 4, sticky = "w")


root.mainloop()