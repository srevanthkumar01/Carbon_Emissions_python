from tkinter import *

from tkinter import messagebox

services = []

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
master.geometry("600x300")
l1 = Label(master, text="count of family members:")
l1.place(x=50, y=28)
l2 = Label(master, text="avg calories:")
l2.place(x=50, y=78)
l3 = Label(master, text="carbon emission")
l3.place(x=50, y=225)

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



CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
#CheckVar4 = IntVar()

l4 = Label(master, text="Utilities")
l4.place(x=50, y=180)

C1 = Checkbutton(master, text = "Electricity ", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(master, text = "Natural Gas", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(master, text = "Fuel ", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
#C4 = Checkbutton(master, text = "Oil ", variable = CheckVar4, \
                 #onvalue = 1, offvalue = 0, height=5, \
                 #width = 20)

def Solution():

    value1= option.get()

    if value1 ==  "Electricity":
        mul=0.12
        res1= (float(result) * mul) * float((CheckVar1.get())==1)
        result1=Label(master,text=res1)
        result1.place(x=50,y=300)

    elif value2 ==  "Natural Gas":
        mul=0.12
        res1= (float(result) * mul) * float((CheckVar2.get())==1)
        result1=Label(master,text=res1)
        result1.place(x=50,y=300)

    elif value3 ==  "Fuel":
        mul=0.12
        res1= (float(result) * mul) * float((CheckVar3.get())==1)
        result1=Label(master,text=res1)
        result1.place(x=50,y=300)

    else:
        print("An option must be selected")



def sol():

    if (CheckVar1.get() == 1) & (CheckVar2.get() == 0) & (CheckVar3.get() == 0):
        l.config(text='Only Electricity used',command=solution())
    elif(CheckVar1.get() == 1) & (CheckVar2.get() == 0) & (CheckVar3.get() == 1):
        l.config(text='Electricity and Fuel used', command=solution())
    elif (CheckVar1.get() == 1) & (CheckVar2.get() == 1) & (CheckVar3.get() == 0):
        l.config(text='Electricity and Natural gas used', command=solution())
    elif (CheckVar1.get() == 1) & (CheckVar2.get() == 1) & (CheckVar3.get() ==1):
        l.config(text='Electricity, Natural gas and Fuel used', command=solution())
    elif (CheckVar1.get() == 0) & (CheckVar2.get() == 0) & (CheckVar3.get() == 1):
        l.config(text='Fuel used', command=solution())
    elif (CheckVar1.get() == 0) & (CheckVar2.get() == 1) & (CheckVar3.get() == 0):
        l.config(text='Natural Gas used', command=solution())
    elif (CheckVar1.get() ==0) & (CheckVar2.get() == 1) & (CheckVar3.get() == 1):
        l.config(text='Natural Gas and Fuel used', command=solution())
    else:
        l.config(text='Did not use any utilities!')


C1.pack()
C2.pack()
C3.pack()
#C4.pack()

master.mainloop()
