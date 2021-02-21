from tkinter import *
from tkinter import messagebox
import os

def deutch():
	os.system(r'C:/"project"/"Нем"/"menu — DE.pyw')

def englash():
	os.system(r'C:/"project"/"Англ"/"menu — ENG.pyw')

def chezka():
	os.system(r'C:/"project"/"Чеш"/"menu — CZ.pyw')


root = Tk()
root.title("Выбор языка")
root.geometry("250x200")
warn = Label(text = "Выберите язык" )
warn.grid(row = 0, column = 5, sticky = "w")


Task = Label(text = "Английский язык")
Task.grid(row = 3, column = 15, sticky = "w")
Task1 = Label(text = "Немецкий язык")
Task1.grid(row = 5, column = 15, sticky = "w")
Task2 = Label(text = "Чешский язык")
Task2.grid(row = 7, column = 15, sticky = "w")

display_button1 = Button(text="→", command = englash )
display_button2 = Button(text="→", command = deutch )
display_button3 = Button(text="→", command = chezka )

display_button1.grid(row = 4, column = 15, sticky = "w")
display_button2.grid(row = 6, column = 15, sticky = "w")
display_button3.grid(row = 8, column = 15, sticky = "w")


root.mainloop()