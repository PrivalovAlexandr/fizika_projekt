from tkinter import *
from tkinter import messagebox
import os

def izotermichesky():
	os.system(r'C:/"project"/"Нем"/"project (izotermichesky) — DE.pyw')

def izobarniy():
	os.system(r'C:/"project"/"Нем"/"project (izobarniy) — DE.pyw')

def izoxorny():
	os.system(r'C:/"project"/"Нем"/"project (izoxorny) — DE.pyw')

def yazik():
	os.system(r'C:/"project"/"Нем"/"vibor — DE.pyw')

def teoriya():
	os.system(r'C:/"project"/"Нем"/"Теория — DE.pyw')

root = Tk()
root.title("Menü")
root.geometry("700x200")
warn = Label(text = "Wählen Sie den Prozess, in dem Sie Ihre Fähigkeiten testen möchten" )
warn.grid(row = 0, column = 7, sticky = "w")


Task = Label(text = "   Isothermer Prozeß")
Task.grid(row = 4, column = 0, sticky = "w")
Task1 = Label(text = "      Isobar Prozeß")
Task1.grid(row = 5, column = 0, sticky = "w")
Task2 = Label(text = "  Helmholtz Prozesß")
Task2.grid(row = 6, column = 0, sticky = "w")
Task3 = Label(text = "       Lokalisierung")
Task3.grid(row = 3, column = 0, sticky = "w")
Task4 = Label(text = "           Theorie")
Task4.grid(row = 7, column = 0, sticky = "w")

display_button1 = Button(text="→", command = izotermichesky )
display_button2 = Button(text="→", command = izobarniy )
display_button3 = Button(text="→", command = izoxorny )
display_button4 = Button(text="Sprache ändern", command = yazik )
display_button5 = Button(text="→", command = teoriya )

display_button1.grid(row = 4, column = 4, sticky = "w")
display_button2.grid(row = 5, column = 4, sticky = "w")
display_button3.grid(row = 6, column = 4, sticky = "w")
display_button4.grid(row = 3, column = 4, sticky = "w")
display_button5.grid(row = 7, column = 4, sticky = "w")


root.mainloop()