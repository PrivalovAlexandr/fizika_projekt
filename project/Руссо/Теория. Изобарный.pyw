from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Теория. Изобарный процесс")
root.geometry("1150x250")

Task = Label(text = "Изобарный процесс")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Изобарным процессом называется процесс, протекающий при неизменном давлении (P=const) и условии m = const и М = const.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Если в некотором процессе не изменяются масса и давление газа, то уравнение Менделеева-Клапейрона для начального и конечного состояний будет:P₁V₁ = RT₁ и P₂V₂ = RT₂")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "При m = const, P = const, V/T = const или V₁/V₂ = T₁/T₂ (уравнение называется законом Гей-Люссака).")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "Состояние газа характеризуется тремя макропараметрами: P — давлением (Постоянный), V — объёмом(Изменяемый), T — температурой.(Изменяемый)")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "Кривая изобарного процесса называется изобарой.")
Task5.grid(row = 6, column = 0, sticky = "w")
Task6 = Label(text = "Изобара, изображенная в прямоугольной системе координат (P – V), по оси ординат которой отсчитывается давление газа, а по оси абсцисс — его объем, является прямой, параллельной оси абсцисс")
Task6.grid(row = 7, column = 0, sticky = "w")
Task7 = Label(text = "Изобара, изображенная в прямоугольной системе координат (V – T), является прямой, проходящей через начало координат")
Task7.grid(row = 8, column = 0, sticky = "w")
Task8 = Label(text = "Изобара, изображенная в прямоугольной системе координат (P – T), является прямой, параллельной оси абсцисс ")
Task8.grid(row = 9, column = 0, sticky = "w")
Task9 = Label(text = "Экспериментальное исследование зависимости объема газа от температуры провел в 1802г. французский физик Жозеф Гей-Люссак.")
Task9.grid(row = 10, column = 0, sticky = "w")
Task10 = Label(text = "Изобарный процесс происходит, например, при нагревании или охлаждении воздуха в стеклянной колбе,соединенной со стеклянной трубкой, отверстие в которой закрыто небольшим столбом жидкости.")
Task10.grid(row = 11, column = 0, sticky = "w")
Task13 = Label(text = "Источник: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()