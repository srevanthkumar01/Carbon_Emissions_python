import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('410x450')
root.title("Project Connect with DBMS")
root.config(background="black")

db = sqlite3.connect("C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS 'people'(name TEXT, phone TEXT)")
db.commit()

textname = StringVar()
textphone = StringVar()
textcountry=StringVar()

def insert():
    name1 = textname.get()
    phone1 = textphone.get()

    conn = sqlite3.connect("C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO 'people' (name,phone) VALUES(?,?)", (name1, phone1))
        db.close()


def show():
    connt = sqlite3.connect("C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db")
    cursor = connt.cursor()
    cursor.execute("SELECT * FROM people")


for row in cursor.fetchall():
    print(row)


lab = Label(root, text="Name")
lab.place(x=0, y=0)

entname = Entry(root, width=20, textvar=textname)
entname.place(x=80, y=0)

lab1 = Label(root, text="Phone")
lab1.place(x=0, y=40)

entphone = Entry(root, width=20, textvar=textphone)
entphone.place(x=80, y=40)

but = Button(root, padx=1, pady=2, text="SUBMIT", command=insert)
but.place(x=60, y=100)

res = Button(root, padx=1, pady=2, text="SHOW", command=insert)
res.place(x=160, y=100)

lab2 = Label(root,text="Countries")
lab.place(x=0, y=300)

countries = ttk.Combobox(root,values=[ "Afghanistan","Africa","Albania","Algeria","Andorra","Angola","Anguilla","Antarctica","Antigua and Barbuda","Argentina","Armenia",
         "Aruba","Asia","Asia (excl. China & India)","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus",
         "Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bonaire Sint Eustatius and Saba","Bosnia and Herzegovina","Botswana","Brazil",
         "British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic",
         "Chad","Chile","China","Christmas Island","Colombia","Comoros","Congo","Cook Islands","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao",
         "Cyprus","Czechia","Democratic Republic of Congo","Denmark","Djibouti","Dominica","Dominican Republic","EU-27","EU-28","Ecuador","Egypt",
         "El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Europe","Europe (excl. EU-27)","Europe (excl. EU-28)",
         "Faeroe Islands","Fiji","Finland","France","French Equatorial Africa","French Guiana","French Polynesia","French West Africa","Gabon",
         "Gambia","Georgia","Germany","Ghana","Greece","Greenland","Grenada","Guadeloupe","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti",
         "Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","International transport","Iran","Iraq","Ireland","Israel","Italy","Jamaica",
         "Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kuwaiti Oil Fires","Kyrgyzstan","Laos","Latvia","Lebanon","Leeward Islands",
         "Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macao","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta",
         "Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Micronesia (country)","Moldova","Mongolia","Montenegro",
         "Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger",
         "Nigeria","Niue","North America","North America (excl. USA)","North Korea","North Macedonia","Norway","Oceania","Oman","Pakistan","Palau",
         "Palestine","Panama","Panama Canal Zone","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion",
         "Romania","Russia","Rwanda","Ryukyu Islands","Saint Helena","Saint Kitts and Nevis","Saint Lucia","Saint Pierre and Miquelon",
         "Saint Vincent and the Grenadines","Samoa","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone",
         "Singapore","Sint Maarten (Dutch part)","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South America","South Korea",
         "South Sudan","Spain","Sri Lanka","St. Kitts-Nevis-Anguilla","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan",
         "Tanzania","Thailand","Timor","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Islands","Tuvalu",
         "Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam",
         "Wallis and Futuna","World","Yemen","Zambia","Zimbabwe"],state="readonly")

#countries = textcountry.get()
#cursor.execute("SELECT Annual_CO2_emissions,year FROM annual WHERE Country=(?)",countries)

print(dict(countries))
#countries.grid(column=1, row=15)
#countries.current(3)
countries.place(x=80, y=200)
"""
# update table

name1 = StringVar()
phone1 = StringVar()


def updatecontact():
    name1 = name1.get()
    print(name1)
    phone1 = phone1.get()
    print(phone1)

    connnt = sqlite3.connect("C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db")
    cursor = connnt.cursor()
    cursor.execute("UPDATE people SET (name,phone) VALUES(?,?)", (name1, phone1))

"""

root.mainloop()



