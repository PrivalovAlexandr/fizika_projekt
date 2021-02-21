from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Theory. Isobaric process")
root.geometry("1150x250")

Task = Label(text = "Isobaric process")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "An Isobaric process is a process that occurs at a constant pressure (p = const) and the condition m = const and M = const.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "If the mass and pressure of the gas do not change in some process, then the Mendeleev-Clapeyron equation for the initial and final States will be: P₁V₁ = RT₁ and P₂V₂ = RT₂")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "For m = const, P = const, V/T = const, or V₁/V₂ = T₁/T₂ (the equation is called the Gay-Lussac's law).")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "The gas state is characterized by three macroparameters: P – pressure (const), V – volume (changing), and T — temperature.(changing)")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "The curve of an Isobaric process is called an Isobar.")
Task5.grid(row = 6, column = 0, sticky = "w")
Task6 = Label(text = "The Isobar depicted in a rectangular coordinate system (P – V), on the ordinate axis of which the gas pressure is calculated, and on the abscissa axis - its volume, is a straight line parallel to the abscissa axis")
Task6.grid(row = 7, column = 0, sticky = "w")
Task7 = Label(text = "An Isobar depicted in a rectangular coordinate system (V – T) is a straight line that passes through the origin")
Task7.grid(row = 8, column = 0, sticky = "w")
Task8 = Label(text = "The Isobar depicted in a rectangular coordinate system (P – T) is a straight line parallel to the abscissa axis")
Task8.grid(row = 9, column = 0, sticky = "w")
Task9 = Label(text = "An experimental study of the dependence of the gas volume on temperature was conducted in 1802 by the French physicist Joseph Gay-Lussac.")
Task9.grid(row = 10, column = 0, sticky = "w")
Task10 = Label(text = "The Isobaric process occurs, for example, when heating or cooling air in a glass flask connected to a glass tube, the hole in which is closed by a small column of liquid.")
Task10.grid(row = 11, column = 0, sticky = "w")
Task13 = Label(text = "Source: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()