import matplotlib.pyplot as plt
import sqlite3
from tkinter import *
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect('C:\\Users\\revwr\\Desktop\\rev1.db')
c = conn.cursor()

#Carbon footprint calculator of an country

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS annual(Country TEXT, Year INTEGER, Annual_CO2_emissions INTEGER)")
"""
def read_from_db():
    c.execute('SELECT * FROM annual')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

read_from_db()
"""

#def graph_data():
#c.execute('SELECT Annual_CO2_emissions,year FROM annual')
#data = c.fetchall()


#global country
#country=country_entry.get()

#global year
#year=year_entry.get()


#user=c.execute("SELECT * FROM annual WHERE Country=? AND Year=? ")
#c.execute(user,(country,year))
#data = c.fetchall()"
j=input("Enter country's name:")
print(j)
c.execute("SELECT Annual_CO2_emissions,year FROM annual WHERE Country= (?) ", [j])
data = c.fetchall()

#c.execute(f"SELECT Annual_CO2_emissions,year FROM annual WHERE Country= {j} ")
#data = c.fetchall()

#c.execute(f"SELECT Country,year FROM annual WHERE Country= {j}")
#data = c.fetchall()


year=[]
emission=[]
country=[]

for row in data:
    #country.append(row[0])
    year.append(row[0])
    emission.append(row[1])

print("Country = ",country)
print("Year = ", year)
print("CO2 emission = ", emission)



plt.plot(emission,year)
plt.ylim()
plt.xlabel("Years")
plt.ylabel("CO2 emissions")
plt.title("Annual CO2 Emission ")


plt.show()

conn = sqlite3.connect('C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db')
c = conn.cursor()

#Carbon footprint calculator of an country

def addNumbers():
    calorie = 0.01
    global res
    res = (float(e2.get()) * calorie) * float(e1.get())
    result = Label(master, text=res, width=20, bg="white")
    result.place(x=50, y=450)
    if (var1.get() & var2.get() & var3.get() & var4.get() == 1):
        c_e = (float(0.12) * res) * float(4)
        c = c_e + res
        print(c)
        l.config(text=c_e)
        l5.config(text=c)
    elif (var1.get() + var2.get() + var3.get() + var4.get() == 2):
        c_e = (float(0.12) * res) * float(2)
        l.config(text=c_e)
        c = c_e + res
        l5.config(text=c)
    elif (var1.get() + var2.get() + var3.get() + var4.get() == 3):
        c_e = (float(0.12) * res) * float(3)
        l.config(text=c_e)
        c = c_e + res
        l5.config(text=c)
    elif (var1.get() + var2.get() + var3.get() + var4.get() == 1):
        c_e = (float(0.12) * res) * float(1)
        l.config(text=c_e)
        c = c_e + res
        l5.config(text=c)
    else:
        l.config(text='please select any')


master = Tk()
master.geometry("800x600")
# bg =PhotoImage(file = "emi2.png")
l1 = Label(master, text="count of family members:")
l1.place(x=50, y=28)
l2 = Label(master, text="avg calories:")
l2.place(x=50, y=78)
l3 = Label(master, text="Total Expenditures")
l3.place(x=50, y=370)
l = Label(master, width=20, bg="white")
l.place(x=50, y=400)


l2 = Label(master, text="Carbon Emission")
l2.place(x=50, y=430)
l3 = Label(master, text="Total Carbon Emissions")
l3.place(x=50, y=470)
l4 = Label(master, text="Country")
l4.place(x=50,y=530)


l5 = Label(master, width=20, bg="white")
l5.place(x=180, y=470)



"""text_box = Text(
    master,
    height=1,
    width=18
)
text_box.place(x=180,y=470)
"""
# inputtxt= master.Text(frame, height = 5, width = 20).place(x=70,y=490)


message = '''
Ways to reduce carbon emissions,

1.Stop buying your water in plastic.

2.Minimize purchases of new products, 
especially resource-intensive, heavy or 
heavily-packaged products.

3.Turn off lights and unplug devices 
when you’re not using them. 

4.Buy locally sourced, organic, plant-based, 
unprocessed foods from local farmers, 
farmers markets, green restaurants and health 
food stores. Minimize food waste by planning 
out meals ahead of time and freezing as much 
as possible.

5.Reduce water use (buy low flow shower and 
faucet heads, water efficient toilets/washing 
machines/dishwashers, check for leaks, buy 
native drought-tolerant plants, etc.).

6.Recycle as much as possible, even when 
travelling, and buy products with 
recycle-able/minimal packaging. Search online
for ways to recycle hard-to-recycle items 
in your local community.

7.Consider installing solar panels on your home.

8.Start a Home Garden.

9.Raise awareness.

10.Use alternative transportation (bus, 
train, carpool, or bike) to get to work 
one day per week.  

 '''


text_box = Text(
    master,
    height=12,
    width=50
)
text_box.place(x=300, y=150)
text_box.insert('end', message)
text_box.config(state='disabled')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
# frame= Frame(master,bg="white",height=200,width=400)
# frame.place(x=250,y=200,height=200,width=200)


# myscrollbar=Scrollbar(frame,orient="vertical")
# myscrollbar.pack(side="right",fill="y")

c1 = Checkbutton(master, text='Electricity', variable=var1, onvalue=1, offvalue=0)
c1.place(x=70, y=160)
c2 = Checkbutton(master, text='Natural Gas', variable=var2, onvalue=1, offvalue=0)
c2.place(x=70, y=200)
c3 = Checkbutton(master, text='Fuel', variable=var3, onvalue=1, offvalue=0)
c3.place(x=70, y=240)
c4 = Checkbutton(master, text='Oil', variable=var4, onvalue=1, offvalue=0)
c4.place(x=70, y=280)
e1 = Entry(master)
e1.place(x=100, y=50)
e2 = Entry(master)
e2.place(x=100, y=100)

e3 = Entry(master)
e3.place(x=100,y=530)
i=e3.get()

b = Button(master, text="Calculate", command=addNumbers, bg="green")
b.place(x=80, y=330)



master.mainloop()