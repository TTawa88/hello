
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Progressbar

brand = ["Audi", "VW", "Seat", "Skoda", "BMW"]
Audi = ["A6", "A4", "A3"]
VW = ["passat", "Golf", "Polo"]
BMW = ["X5", "X3"]


window = Tk()
window.title("Byte Switch")
window.geometry('800x400')

combo = Combobox(window)
combo['values'] = (brand)
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=0)

# btn = Button(window, text="Не нажимать!")
# btn.grid(column=1, row=0)
window.mainloop()
