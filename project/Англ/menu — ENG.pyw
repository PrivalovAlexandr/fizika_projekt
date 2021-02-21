from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Англ"/"project (izotermichesky) — ENG.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Англ"/"project (izobarniy) — ENG.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Англ"/"project (izoxorny) — ENG.pyw')

def yazik():
	os.system(r'C:/"project"/"Англ"/"vibor — ENG.pyw')

def teoriya():
	os.system(r'C:/"project"/"Англ"/"Теория — ENG.pyw')

root = Tk()
root.title("Menu")
root.geometry("700x200")
warn = Label(text = "Select the process by which you want to test your skills" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = " Isothermal process")
Task.grid(row = 4, column = 0, sticky = "w")
Task1 = Label(text = "    Isobaric process")
Task1.grid(row = 5, column = 0, sticky = "w")
Task2 = Label(text = "   Isochoric process")
Task2.grid(row = 6, column = 0, sticky = "w")
Task3 = Label(text = "         Localization")
Task3.grid(row = 3, column = 0, sticky = "w")
Task4 = Label(text = "             Theory")
Task4.grid(row = 7, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )
display_button4 = Button(text="Changing the language", command = yazik )
display_button5 = Button(text="→", command = teoriya )

display_button1.grid(row = 4, column = 4, sticky = "w")
display_button2.grid(row = 5, column = 4, sticky = "w")
display_button3.grid(row = 6, column = 4, sticky = "w")
display_button4.grid(row = 3, column = 4, sticky = "w")
display_button5.grid(row = 7, column = 4, sticky = "w")


root.mainloop()