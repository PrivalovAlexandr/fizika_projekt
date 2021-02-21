from tkinter import *
from tkinter import messagebox

a = "nothing"

def result():
	t = ent.get()
	t1 = ent1.get()
	t2 = ent2.get()
	t3 = ent3.get()
	t4 = ent4.get()
	t5 = ent5.get()
	res = 2.0

	if t == "2":
		res1 = res + 0.16
	else:
		res1 = res + 0
	if t1 == "1":
		res2 = res1 + 0.16
	else:
		res2 = res1 + 0
	if t2 == "1":
		res3 = res2 + 0.18
	else:
		res3 = res2 + 0
	if t3 == "2":
		res4 = res3 + 0.16
	else:
		res4 = res3 + 0	 
	if t4 == "V/T=const":
		res5 = res4 + 1
	else:
		res5 = res4 + 0
	if t5 == "Gesetz Von Gay-Lussac":
		res6 = res5 + 1
	else:
		res6 = res5 + 0	
	
	lab = Label(text= round (res6) )
	lab.grid(row = 8, column = 1, sticky = "w")



root = Tk()
root.title("Gasgesetze. Isobar Prozeß")
root.geometry("900x200")
warn = Label(text = "Geben Sie die Zahl der Option ein, die Sie im Feld unten ausgewählt haben. Es gibt zwei Optionen: 1 - veränderbar und 2 - const.")
warn.grid(row = 0, column = 0, sticky = "w")

Task9 = Label(text = "Die Formel wird mit allen Zeichen ohne Leerzeichen eingegeben! Der name des Gesetzes beginnt mit dem Wort <<Gesetz>>" )
Task9.grid(row = 1, column = 0, sticky = "w")
Task = Label(text = "Geben Sie den Wert p ein, bei dem der isobare Prozeß ausgeführt wird: ")
Task.grid(row = 2, column = 0, sticky = "w")
Task1 = Label(text = "Geben Sie den Wert V ein, bei dem der isobare Prozeß ausgeführt wird: ")
Task1.grid(row = 3, column = 0, sticky = "w")
Task2 = Label(text = "Geben Sie den Wert T ein, bei dem der isobare Prozeß ausgeführt wird: ")
Task2.grid(row = 4, column = 0, sticky = "w")
Task3 = Label(text = "Geben Sie den Wert m ein, bei dem der isobare Prozeß ausgeführt wird: ")
Task3.grid(row = 5, column = 0, sticky = "w")
Task4 = Label(text = "Formel eingeben: ")
Task4.grid(row = 6, column = 0, sticky = "w")
Task5 = Label(text = "Geben Sie den Namen des Gesetzes ein: ")
Task5.grid(row = 7, column = 0, sticky = "w")

ent = Entry()
ent.grid(row = 2, column = 1, sticky = "e")
ent1 = Entry()
ent1.grid(row = 3, column = 1, sticky = "e")
ent2 = Entry()
ent2.grid(row = 4, column = 1, sticky = "e")
ent3 = Entry()
ent3.grid(row = 5, column = 1, sticky = "e")
ent4 = Entry()
ent4.grid(row = 6, column = 1, sticky = "e")
ent5 = Entry()
ent5.grid(row = 7, column = 1, sticky = "e")


display_button = Button(text="Antwort überprüfen", command = result)

display_button.grid(row = 8, column = 1, sticky = "e")


root.mainloop()