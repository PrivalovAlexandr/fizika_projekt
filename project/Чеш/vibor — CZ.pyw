from tkinter import *
from tkinter import messagebox
import os

def deutch():
	os.system(r'C:/"project"/"Нем"/"menu — DE.pyw')

def englash():
	os.system(r'C:/"project"/"Англ"/"menu — ENG.pyw')

def rusnya():
	os.system(r'C:/"project"/"Руссо"/"menu.pyw')


root = Tk()
root.title("Výběr jazyka")
root.geometry("250x200")
warn = Label(text = "Vyberte jazyk" )
warn.grid(row = 0, column = 5, sticky = "w")


Task = Label(text = "Angličtina")
Task.grid(row = 3, column = 15, sticky = "w")
Task1 = Label(text = "Němčina")
Task1.grid(row = 5, column = 15, sticky = "w")
Task2 = Label(text = "Ruský jazyk")
Task2.grid(row = 7, column = 15, sticky = "w")

display_button1 = Button(text="→", command = englash )
display_button2 = Button(text="→", command = deutch )
display_button3 = Button(text="→", command = rusnya )

display_button1.grid(row = 4, column = 15, sticky = "w")
display_button2.grid(row = 6, column = 15, sticky = "w")
display_button3.grid(row = 8, column = 15, sticky = "w")


root.mainloop()