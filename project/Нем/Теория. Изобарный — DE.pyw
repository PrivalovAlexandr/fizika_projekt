from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Theorie. Isobar Prozeß")
root.geometry("1150x250")

Task = Label(text = "Isobar Prozeß")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Der isobare Prozeß wird als Prozess bezeichnet, der bei unverändertem Druck (P = Konstante) und der Bedingung m = Konstante und M = Konstante abläuft.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Wenn in einem Prozeß ändert nicht die Masse und der Druck des Gases, das die Gleichung Mendelejew-Klapeyron für Start-und End-Zustände wird:P1V1 = RT₁ und P₂V₂ = RT₂")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Bei m = Konstante, p = Konstante, V/T = Konstante oder V₁/V₂ = T1/T₂ (die Gleichung wird als Gay-Lussac-Gesetz bezeichnet).")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "Der Zustand des Gases ist durch drei Makroparameter gekennzeichnet: P-Druck(Konstante), V — Volumen (Variiert), T — Temperatur.(Variiert)")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "Der Zustand des Gases wird durch drei Kurve isobar Prozeß isobar genannt gekennzeichnet.")
Task5.grid(row = 6, column = 0, sticky = "w")
Task6 = Label(text = "Isobar, dargestellt im kartesischen Koordinatensystem (P – V), auf der Y-Achse beginnt mit dem Druck des Gases, und die X—Achse ist das Volumen, ist eine gerade parallel zur Abszisse")
Task6.grid(row = 7, column = 0, sticky = "w")
Task7 = Label(text = "Isobar, die im rechteckigen Koordinatensystem (V – T) abgebildete isobar ist eine gerade Linie, die den Ursprung durchläuft")
Task7.grid(row = 8, column = 0, sticky = "w")
Task8 = Label(text = "Isobar, dargestellt in einem rechteckigen Koordinatensystem (P – T), ist eine gerade parallel zur Achse der Abszisse")
Task8.grid(row = 9, column = 0, sticky = "w")
Task9 = Label(text = "Experimentelle Untersuchung der Abhängigkeit des gasvolumens von der Temperatur in 1802 Jahre. der französische Physiker Joseph Gay-Lussac.")
Task9.grid(row = 10, column = 0, sticky = "w")
Task10 = Label(text = "Der isobare Prozeß tritt beispielsweise beim erhitzen oder kühlen von Luft in einem Glaskolben auf,der mit einem Glasrohr verbunden ist, dessen öffnung durch eine kleine flüssigkeitssäule geschlossen ist.")
Task10.grid(row = 11, column = 0, sticky = "w")
Task13 = Label(text = "Quelle: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()