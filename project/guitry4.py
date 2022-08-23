from tkinter import *

from tkinter import messagebox

services = []

def showInfo():
    for i in range(len(services)):
        selected=" "
        if services[i].get()>=1:
            selected += str(1)
            messagebox.showinfo(message="You selected Checkbox" +selected)


window = Tk()
window.title=("Checkbox Buttons")

for i in range (4):
    option=IntVar()
    option.set(0)
    services.append(option)

Checkbutton(window, text="Electricity",
variable=services[0]).pack()

Checkbutton(window, text="Natural Gas",
variable=services[1]).pack()

Checkbutton(window, text="Fuel",
variable=services[2]).pack()

Checkbutton(window, text="Oil",
variable=services[3]).pack()

Button(window,text="ok",
       command=showInfo()).pack()

window.mainloop()