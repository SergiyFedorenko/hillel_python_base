from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Frame, Label
from tkinter import Tk
import tkinter.font as font
import sys
#Making a win
win = Tk()
win.title("Розрахунок даху 1.0")
win.geometry('650x350')
big_font = font.Font(size=16)
#Giving a Function To The Button
def btn1():
  ga = ((float(number_b.get()) /2) **2 + (float(number_f.get()) **2))**0.5
  answers_ga.insert(0, "Ga = " + str(ga))
  c = ((ga) **2 + (float(number_a.get()) /2) **2) **0.5
  answers_c.insert(0, "C = " + str(c))
  gb = ((float(number_a.get()) /2) **2 + (float(number_f.get()) **2))**0.5
  answers_gb.insert(0, "Gb = " + str(gb))
  print("Готово")
lbl_c = Label(text="Ребро даху C", font=("Times", 14, "bold"), background="#abafff", foreground="#ff081e")  
lbl_c.place(x=280, y=25)
lbl_ga = Label(text="Довжина ската G-a", font=("Times", 14, "bold"), background="#abafff", foreground="#000080")
lbl_ga.place(x=280, y=55)
lbl_gb = Label(text="Довжина ската G-b", font=("Times", 14, "bold"), background="#abafff", foreground="#0e8500")
lbl_gb.place(x=280, y=80)
#image
path = 'trik2.gif'
img = ImageTk.PhotoImage(Image.open(path))
lbl = Label(win, image = img)
lbl.grid(column=0, row=0)
# написи
label_a = Label(text="Довжина, a", font=("Times", 14, "bold"), background="#f4ff87", foreground="#000080")
label_a.place(x=30, y=210)
label_b = Label(text="Ширина, b", font=("Times", 14, "bold"), background="#f4ff87", foreground="#0e8500")
label_b.place(x=30, y=240)
label_f = Label(text="Висота, f", font=("Times", 14, "bold"), background="#f4ff87", foreground="#eb00c0")
label_f.place(x=30, y=270)
#ячейки ввода
number_a = Entry(font=("Times", 14, "bold"), justify="center", background="#f4ff87", foreground="#000080", width=5)
number_a.place(x=150, y=210)
number_b = Entry(font=("Times", 14, "bold"), justify="center", background="#f4ff87", foreground="#0e8500", width=5)
number_b.place(x=150, y=240)
number_f = Entry(font=("Times", 14, "bold"), justify="center", background="#f4ff87", foreground="#eb00c0", width=5)
number_f.place(x=150, y=270)
#ячейки виводу
answers_c = Listbox(font=big_font, width=12, heigh=1)
answers_c.place(x=480, y=25)
answers_ga = Listbox(font=big_font, width=12, heigh=1)
answers_ga.place(x=480, y=55)
answers_gb = Listbox(font=big_font, width=12, heigh=1)
answers_gb.place(x=480, y=80)
#Making The Button
button1 =  Button(win, text="Розрахувати", font=big_font, command=btn1)
button1.grid(column=2, row=2)

win.mainloop()
#NB:This Python programme Will Print Something In The Terminal
#Check My Account To See How We Print On The Screen Or Type In Google "Tkinter Label"