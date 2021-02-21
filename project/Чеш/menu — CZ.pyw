from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Чеш"/"project (izotermichesky) — CZ.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Чеш"/"project (izobarniy) — CZ.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Чеш"/"project (izoxorny) — CZ.pyw')

def yazik():
	os.system(r'C:/"project"/"Чеш"/"vibor — CZ.pyw')

def teoriya():
	os.system(r'C:/"project"/"Чеш"/"Теория — CZ.pyw')

root = Tk()
root.title("Menu")
root.geometry("700x200")
warn = Label(text = "Vyberte proces, kterým chcete vyzkoušet své dovednosti" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "Izotermický proces")
Task.grid(row = 4, column = 0, sticky = "w")
Task1 = Label(text = "     Изобарный процесс")
Task1.grid(row = 5, column = 0, sticky = "w")
Task2 = Label(text = "     Izobarický proces")
Task2.grid(row = 6, column = 0, sticky = "w")
Task3 = Label(text = "            Lokalizace")
Task3.grid(row = 3, column = 0, sticky = "w")
Task4 = Label(text = "                 Teorie")
Task4.grid(row = 7, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )
display_button4 = Button(text="Změna jazyka", command = yazik )
display_button5 = Button(text="→", command = teoriya )

display_button1.grid(row = 4, column = 4, sticky = "w")
display_button2.grid(row = 5, column = 4, sticky = "w")
display_button3.grid(row = 6, column = 4, sticky = "w")
display_button4.grid(row = 3, column = 4, sticky = "w")
display_button5.grid(row = 7, column = 4, sticky = "w")


root.mainloop()