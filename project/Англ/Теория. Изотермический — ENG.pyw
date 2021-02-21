from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Theory. Isothermal process")
root.geometry("1000x300")

Task = Label(text = "Isothermal process")
Task.grid(row = 1, column = 5, sticky = "w")
Task1 = Label(text = "If the mass and temperature of the gas do not change in some process, then this process is called isothermal. When m = const T = const P₁V₁ = P₂V₂ or PV = const.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "The resulting PV = const equation is called the isothermal process equation.")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "This equation was obtained by the English physicist Robert Boyle in 1662 and the French physicist Edme Mariotte in 1676,")
Task3.grid(row = 4, column = 0, sticky = "w")
Task9 = Label(text = "and he also derived the formula p*V=const (Boyle–Mariotte law)")
Task9.grid(row = 5, column = 0, sticky = "w")
Task4 = Label(text = "The gas state is characterized by three macroparameters: P-pressure (changing), V-volume (changing), and T — temperature.(const)")
Task4.grid(row = 6, column = 0, sticky = "w")
Task5 = Label(text = "Only two parameters can be specified for a graphical representation of a process,")
Task5.grid(row = 7, column = 0, sticky = "w")
Task10 = Label(text = "which change, so the same process can be represented in three coordinate planes: (P – V), (V – T), (P – T).")
Task10.grid(row =8 , column = 0, sticky = "w")
Task6 = Label(text = "The graph of an isothermal process is called an isotherm. An isotherm depicted in a rectangular coordinate system (P – V),")
Task6.grid(row = 9, column = 0, sticky = "w")
Task12 = Label(text = "on the ordinate axis of which the gas pressure is counted, and on the abscissa axis - its volume, is a hyperbola.")
Task12.grid(row = 10, column = 0, sticky = "w")
Task7 = Label(text = "The isotherm depicted in a rectangular coordinate system (V – T) is a straight line parallel to the ordinate axis")
Task7.grid(row = 11, column = 0, sticky = "w")
Task8 = Label(text = "The isotherm depicted in a rectangular coordinate system (P – T) is a straight line parallel to the ordinate axis ")
Task8.grid(row = 12, column = 0, sticky = "w")
Task13 = Label(text = "Source: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()