from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Teorie. Izobarický děj")
root.geometry("1150x250")

Task = Label(text = "Izobarický děj")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "Izobarický děj se nazývá proces, který teče při nezměněném tlaku (P = konst) a za předpokladu m = konst a M = konst.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Pokud je v nějakém procesu, nemění se hmotnost a tlak plynu, pak rovnice Mendeleeva-Clapeyron pro počáteční a konečné stavy budou:P1V1 = RT1 a P2V2 = RT2")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Při m = konst, P = konst, V / T = konst nebo V1 / V2 = T1 / T2 (rovnice se nazývá Gay-Lussac's law).")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "Stav plynu je charakterizován třemi makroparametry: P-tlakem (konst), v — objemem(změna), t-teplotou.(změna)")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "Křivka izobarického procesu se nazývá izobara.")
Task5.grid(row = 6, column = 0, sticky = "w")
Task6 = Label(text = "Izobara znázorněná v pravoúhlém souřadnicovém systému (P – V), jehož osa je vypočtena tlakem plynu a osa absciss-jeho objem, je rovná, rovnoběžná s osou absciss")
Task6.grid(row = 7, column = 0, sticky = "w")
Task7 = Label(text = "Isobara, zobrazená v obdélníkovém souřadnicovém systému (V – T), je přímá, procházející začátkem souřadnic")
Task7.grid(row = 8, column = 0, sticky = "w")
Task8 = Label(text = "Izobara, zobrazená v pravoúhlém souřadném systému (P – T), je rovná, rovnoběžná osa absciss")
Task8.grid(row = 9, column = 0, sticky = "w")
Task9 = Label(text = "Experimentální studii závislosti objemu plynu na teplotě provedl v roce 1802 francouzský fyzik Joseph Gay-Lucsac.")
Task9.grid(row = 10, column = 0, sticky = "w")
Task10 = Label(text = "Isobarický děj se vyskytuje například při ohřevu nebo chlazení vzduchu ve skleněné baňce připojené ke skleněné trubce, jejíž otvor je uzavřen malým sloupkem kapaliny.")
Task10.grid(row = 11, column = 0, sticky = "w")
Task13 = Label(text = "Zdroj: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()