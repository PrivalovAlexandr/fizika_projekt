from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Teorie. Izotermický děj")
root.geometry("1000x300")

Task = Label(text = "Izotermický děj")
Task.grid(row = 1, column = 5, sticky = "w")
Task1 = Label(text = "Pokud se v určitém procesu nezmění hmotnost a teplota plynu, pak se tento proces nazývá izotermický. Při m = konst T = konst P1V1 = P2V2 nebo PV = konst.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Výsledná rovnice PV = konst se nazývá rovnice izotermického procesu.")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "Tato rovnice byla získána anglickým fyzikem Robertem Boylem v roce 1662 a francouzským fyzikem Edmonem Mariottem v roce 1676,")
Task3.grid(row = 4, column = 0, sticky = "w")
Task9 = Label(text = "stejně jako on vyvedl vzorec p*V = konst (Boyleův–Mariottův zákon)")
Task9.grid(row = 5, column = 0, sticky = "w")
Task4 = Label(text = "Stav plynu je charakterizován třemi makroparametry: p — tlakem (změna), V — objemem (změna), T — teplotou.(konst)")
Task4.grid(row = 6, column = 0, sticky = "w")
Task5 = Label(text = "Při grafickém zobrazení procesu lze určit pouze dva parametry,")
Task5.grid(row = 7, column = 0, sticky = "w")
Task10 = Label(text = "které se liší, takže jeden a týž proces lze shrnout do tří koordinovat rovinách: (P – V), (V – T), (P – T).")
Task10.grid(row =8 , column = 0, sticky = "w")
Task6 = Label(text = "Graf izotermického procesu se nazývá izoterma. Izoterma zobrazená v pravoúhlém souřadném systému (P-V),")
Task6.grid(row = 9, column = 0, sticky = "w")
Task12 = Label(text = "v ose Y, která počítá tlak plynu a v ose X – jeho objem, je nadsázka.")
Task12.grid(row = 10, column = 0, sticky = "w")
Task7 = Label(text = "Izoterma zobrazená v pravoúhlém souřadnicovém systému (V – T) je přímá, rovnoběžná s osou ordinátu")
Task7.grid(row = 11, column = 0, sticky = "w")
Task8 = Label(text = "Izoterma zobrazená v pravoúhlém souřadnicovém systému (P – T) je přímá, rovnoběžná s osou ordinátu.")
Task8.grid(row = 12, column = 0, sticky = "w")
Task13 = Label(text = "Zdroj: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
Task.grid(row = 1, column = 0, sticky = "w")

root.mainloop()