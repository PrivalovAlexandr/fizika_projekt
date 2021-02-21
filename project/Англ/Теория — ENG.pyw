from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Англ"/"Теория. Изотермический — ENG.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Англ"/"Теория. Изобарный — ENG.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Англ"/"Теория. Изохорный — ENG.pyw')

root = Tk()
root.title("Menu")
root.geometry("700x200")
warn = Label(text = "Select the process by which you want to add to your knowledge" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "Isothermal process")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Isobaric process")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Isochoric process")
Task2.grid(row = 3, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )

display_button1.grid(row = 1, column = 4, sticky = "w")
display_button2.grid(row = 2, column = 4, sticky = "w")
display_button3.grid(row = 3, column = 4, sticky = "w")


root.mainloop()