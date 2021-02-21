from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Theorie. Isothermer Prozeß")
root.geometry("1000x300")

Task = Label(text = "Isothermer Prozeß")
Task.grid(row = 1, column = 5, sticky = "w")
Task1 = Label(text = "Wenn sich die Masse und die Temperatur des Gases in einem Prozeß nicht ändern, wird ein solcher Prozeß als isotherm bezeichnet. Bei m = Konstante T = Konstante P1V1 = P₂V₂ oder PV = Konstante.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Die resultierende PV = Konstante Gleichung wird als Isotherme prozeßgleichung bezeichnet.")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Diese Gleichung wurde 1662 vom englischen Physiker Robert Boyle und 1676 vom französischen Physiker Edmond Mariott erhalten,")
Task3.grid(row = 4, column = 0, sticky = "w")
Task9 = Label(text = "sowie er führte die Formel p*V = Konstante (Gesetz von Boyle-Mariotte)")
Task9.grid(row = 5, column = 0, sticky = "w")
Task4 = Label(text = "Der Zustand des Gases ist durch drei Makroparameter gekennzeichnet: P-Druck(Variiert), V — Volumen (Variiert), T — Temperatur.(Konstante)")
Task4.grid(row = 6, column = 0, sticky = "w")
Task5 = Label(text = "Wenn Sie einen Prozess grafisch darstellen, können Sie nur zwei Parameter angeben,")
Task5.grid(row = 7, column = 0, sticky = "w")
Task10 = Label(text = "die sich ändern, sodass derselbe Prozess in drei koordinatenebenen dargestellt werden kann: (P – V), (V – T), (P – T).")
Task10.grid(row =8 , column = 0, sticky = "w")
Task6 = Label(text = "Das Diagramm des isothermen Prozesses wird als Isotherme bezeichnet. Isotherme, dargestellt in einem rechteckigen Koordinatensystem (P – V),")
Task6.grid(row = 9, column = 0, sticky = "w")
Task12 = Label(text = "auf der Achse des ordinats, die den Gasdruck und die Abszisse — sein Volumen berechnet, ist Hyperbel.")
Task12.grid(row = 10, column = 0, sticky = "w")
Task7 = Label(text = "Die in einem rechteckigen Koordinatensystem (V – T) abgebildete Isotherme ist eine gerade parallel zur Achse des ordinats")
Task7.grid(row = 11, column = 0, sticky = "w")
Task8 = Label(text = "Die in einem rechteckigen Koordinatensystem (P – T) abgebildete Isotherme ist eine gerade parallel zur Achse des ordinats")
Task8.grid(row = 12, column = 0, sticky = "w")
Task13 = Label(text = "Quelle: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()