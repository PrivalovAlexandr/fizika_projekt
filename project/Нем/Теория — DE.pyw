from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Нем"/"Теория. Изотермический — DE.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Нем"/"Теория. Изобарный — DE.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Нем"/"Теория. Изохорный — DE.pyw')

root = Tk()
root.title("Theorie")
root.geometry("700x200")
warn = Label(text = "Wählen Sie den Prozeß, durch den Sie Ihr wissen ergänzen möchten" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "Isothermer Prozeß")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Isobar Prozeß")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Helmholtz Prozesß")
Task2.grid(row = 3, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )

display_button1.grid(row = 1, column = 4, sticky = "w")
display_button2.grid(row = 2, column = 4, sticky = "w")
display_button3.grid(row = 3, column = 4, sticky = "w")


root.mainloop()