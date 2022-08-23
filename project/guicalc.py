from tkinter import*

def addNumbers():
    calorie=0.01
    global res
    res=(float(e2.get())*calorie)*float(e1.get())
    result=Label(master, text=res , width=20,bg="white")
    result.place(x=50,y=450)
    if (var1.get()&var2.get()&var3.get()&var4.get() == 1):
            c_e=(float(1.12)*res)*float(4)
            l.config(text=c_e)
    elif (var1.get()+var2.get()+var3.get()+var4.get() == 2):
        c_e=(float(1.12)*res)*float(2)
        l.config(text=c_e)
    elif (var1.get()+var2.get()+var3.get()+var4.get() == 3):
        c_e=(float(1.12)*res)*float(3)
        l.config(text=c_e)
    elif (var1.get()+var2.get()+var3.get()+var4.get() == 1):
        c_e=(float(1.12)*res)*float(1)
        l.config(text=c_e)
    else:
            l.config(text='please select any')
master=Tk()
master.geometry("500x500")
#bg =PhotoImage(file = "emi2.png")
l1=Label(master, text="count of family members:")
l1.place(x=50,y=28)
l2=Label(master, text="avg calories:")
l2.place(x=50,y=78)
l3=Label(master,text="Total Expenditures")
l3.place(x=50,y=370)
l = Label(master, width=20,bg="white")
l.place(x=50,y=400)
l2 = Label(master,text="Carbon Emission")
l2.place(x=50,y=430)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
frame= Frame(master,bg="white",height=200,width=400)
frame.place(x=250,y=200,height=200,width=200)

myscrollbar=Scrollbar(frame,orient="vertical")
myscrollbar.pack(side="right",fill="y")

c1 = Checkbutton(master, text='Electricity',variable=var1, onvalue=1, offvalue=0)
c1.place(x=70,y=160)
c2 = Checkbutton(master, text='Natural Gas',variable=var2, onvalue=1, offvalue=0)
c2.place(x=70,y=200)
c3 = Checkbutton(master, text='Fuel',variable=var3, onvalue=1, offvalue=0)
c3.place(x=70,y=240)
c4 = Checkbutton(master, text='Oil',variable=var4, onvalue=1, offvalue=0)
c4.place(x=70,y=280)
e1=Entry(master)
e1.place(x=100,y=50)
e2=Entry(master)
e2.place(x=100,y=100)
b = Button(master, text="Calculate", command=addNumbers,bg="green")
b.place(x=80,y=330)
master.mainloop()