from tkinter import *


def addNumbers():
    value = option.get()
    if value == "VEG":
        calorie = 0.005
        res = (float(e2.get()) * calorie) * float(e1.get())
        result = Label(master, text=res)
        result.place(x=50, y=200)
    elif value == "NON":
        calorie1 = 0.01
        res = (float(e2.get()) * calorie1) * float(e1.get())
        result = Label(master, text=res)
        result.place(x=50, y=200)
    else:
        print("An option must be selected")


master = Tk()
master.geometry("500x500")
l1 = Label(master, text="count of family members:")
l1.place(x=50, y=28)
l2 = Label(master, text="avg calories:")
l2.place(x=50, y=78)
l3 = Label(master, text="Utilities used:")
l2.place(x=50, y=128)





l = Label(master, text="carbon emission")
l.place(x=50, y=225)



e1 = Entry(master)
e1.place(x=100, y=50)
e2 = Entry(master)
e2.place(x=100, y=100)
option = StringVar()
R1 = Radiobutton(master, text="VEG", value="VEG", var=option)
R1.place(x=50, y=130)
R2 = Radiobutton(master, text="NON-VEG", value="NON", var=option)
R2.place(x=130, y=130)
b = Button(master, text="Calculate", command=addNumbers)
b.place(x=150, y=200)

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()

Button1 = Checkbutton(master, text = "Electricity",
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button2 = Checkbutton(master, text = "Natural Gas",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button3 = Checkbutton(master, text = "Fuel",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button4 = Checkbutton(master, text = "Oil",
                      variable = Checkbutton4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)


Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()

master.mainloop()