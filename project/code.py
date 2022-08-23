from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from login import Log
from register import Register

''' Window Setting Start '''
# Creating Widget
system = tk.Tk()

# Creating size of window
system.geometry('600x600')

# Background Colors
system.configure(background='BLACK')

# Locking the window size
system.resizable(width=False, height=False)

# Creating Title
system.title('Login and Registration System')

''' Window Setting End '''

# Top Frame
top_frame = Label(system, text='CO2 Emissions', font=('Cosmic', 25, 'bold'), bg='WHITE', relief='groove', padx=500,
                  pady=30)
top_frame.pack(side='top')

# Creating Frame
frame = LabelFrame(system, text='Please LOGIN or REGISTER to continue', padx=30, pady=40, bg='white', bd='5',
                   relief='groove')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Creating login button and positioning it
login = tk.Button(frame, text="LOGIN", width="10", bd='3', command=Log, font=('Times', 12, 'bold'), bg='PINK',
                  relief='groove', justify='center', pady='5')
login.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating and Positioning Button in Main Frame
register = tk.Button(frame, text="REGISTER", width="10", bd='3', command=Register, font=('Times', 12, 'bold'),
                     bg='BROWN', fg='BLACK', relief='groove', justify='center', pady='5')
register.pack()


# Quit Button of main frame

def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass


Quit = tk.Button(system, text="Quit", width="10", command=Quit, bd='3', font=('Times', 12, 'bold'), bg='WHITE',
                 fg='BLACK', relief='groove', justify='center', pady='5')
Quit.place(anchor='sw', rely=1, relx=0.775)

# Displyaing Widget to Screen
system.mainloop()



