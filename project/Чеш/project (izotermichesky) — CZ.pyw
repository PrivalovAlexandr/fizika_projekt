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

	if t == "1":
		res1 = res + 0.16
	else:
		res1 = res + 0
	if t1 == "1":
		res2 = res1 + 0.16
	else:
		res2 = res1 + 0
	if t2 == "2":
		res3 = res2 + 0.18
	else:
		res3 = res2 + 0
	if t3 == "2":
		res4 = res3 + 0.16
	else:
		res4 = res3 + 0	 
	if t4 == "p*V=konst":
		res5 = res4 + 1
	else:
		res5 = res4 + 0
	if t5 == "Boyleův–Mariottův zákon":
		res6 = res5 + 1
	else:
		res6 = res5 + 0
	
	

	lab = Label(text= round(res6) )
	lab.grid(row = 8, column = 1, sticky = "w")
    


root = Tk()
root.title("Plynové zákony. Izotermický děj")
root.geometry("1400x200")
warn = Label(text = "Zadejte číslo možnosti, kterou jste vybrali v níže uvedeném poli. Existují dvě možnosti: 1 - změna a 2 - const. Vzorec vstoupit se všemi znaky bez mezer! Název zákona obsahuje slovo <<zákon>>" )
warn.grid(row = 0, column = 0, sticky = "w")

Task = Label(text = "Zadejte hodnotu p, ve které bude proveden izotermický děj: ")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Zadejte hodnotu V, ve které bude proveden izotermický děj: ")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Zadejte hodnotu T, ve které bude proveden izotermický děj: ")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Zadejte hodnotu m, ve které bude proveden izotermický děj: ")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "Zadejte vzorec: ")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "Zadejte název zákona: ")
Task5.grid(row = 6, column = 0, sticky = "w")

ent = Entry()
ent.grid(row = 1, column = 1, sticky = "e")
ent1 = Entry()
ent1.grid(row = 2, column = 1, sticky = "e")
ent2 = Entry()
ent2.grid(row = 3, column = 1, sticky = "e")
ent3 = Entry()
ent3.grid(row = 4, column = 1, sticky = "e")
ent4 = Entry()
ent4.grid(row = 5, column = 1, sticky = "e")
ent5 = Entry()
ent5.grid(row = 6, column = 1, sticky = "e")

display_button = Button(text="Zkontrolujte odpověď", command = result)

display_button.grid(row = 7, column = 1, sticky = "e")


root.mainloop()