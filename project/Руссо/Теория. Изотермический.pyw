from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Теория. Изотермический процесс")
root.geometry("1000x300")

Task = Label(text = "Изотермический процесс")
Task.grid(row = 1, column = 5, sticky = "w")
Task1 = Label(text = "Если в некотором процессе не изменяются масса и температура газа, то такой процесс называется изотермическим. При m = const T = const P₁V₁ = P₂V₂ или PV = const.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Полученное PV = const уравнение называется уравнением изотермического процесса.")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Это уравнение было получено английским физиком Робертом Бойлем в 1662 году и французским физиком Эдмоном Мариоттом в 1676г,")
Task3.grid(row = 4, column = 0, sticky = "w")
Task9 = Label(text = "а так же он вывел формулу p*V=const (Закон Бойля-Мариотта)")
Task9.grid(row = 5, column = 0, sticky = "w")
Task4 = Label(text = "Состояние газа характеризуется тремя макропараметрами: P — давлением (Изменяемый), V — объёмом(Изменяемый), T — температурой.(Постоянный)")
Task4.grid(row = 6, column = 0, sticky = "w")
Task5 = Label(text = "При графическом изображении процесса можно указать только два параметра,")
Task5.grid(row = 7, column = 0, sticky = "w")
Task10 = Label(text = "которые изменяются, поэтому один и тот же процесс можно представить в трёх координатных плоскостях: (Р – V), (V – T), (P – T).")
Task10.grid(row =8 , column = 0, sticky = "w")
Task6 = Label(text = "График изотермического процесса называется изотермой. Изотерма, изображенная в прямоугольной системе координат (P – V),")
Task6.grid(row = 9, column = 0, sticky = "w")
Task12 = Label(text = "по оси ординат которой отсчитывается давление газа, а по оси абсцисс — его объем, является гиперболой.")
Task12.grid(row = 10, column = 0, sticky = "w")
Task7 = Label(text = "Изотерма, изображенная в прямоугольной системе координат (V – T), является прямой, параллельной оси ординат")
Task7.grid(row = 11, column = 0, sticky = "w")
Task8 = Label(text = "Изотерма, изображенная в прямоугольной системе координат (P – T), является прямой, параллельной оси ординат ")
Task8.grid(row = 12, column = 0, sticky = "w")
Task13 = Label(text = "Источник: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()