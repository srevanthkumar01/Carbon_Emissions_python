import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_269=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_269["font"] = ft
        GLabel_269["fg"] = "#333333"
        GLabel_269["justify"] = "center"
        GLabel_269["text"] = ("Are you a vegetarian or a non-vegetarian?")
        GLabel_269.place(x=50,y=30,width=300,height=25)

        GRadio_867=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_867["font"] = ft
        GRadio_867["fg"] = "#333333"
        GRadio_867["justify"] = "center"
        GRadio_867["text"] = "Vegetarian"
        GRadio_867.place(x=80,y=80,width=85,height=25)
        GRadio_867["command"] = self.GRadio_867_command

        GRadio_260=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_260["font"] = ft
        GRadio_260["fg"] = "#333333"
        GRadio_260["justify"] = "center"
        GRadio_260["text"] = "Non-vegitarian"
        GRadio_260.place(x=200,y=80,width=100,height=25)
        GRadio_260["command"] = self.GRadio_260_command

        GLabel_318=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "Enter number of family members"
        GLabel_318.place(x=60,y=140,width=300,height=25)

        GLineEdit_327=tk.Entry(root)
        GLineEdit_327["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_327["font"] = ft
        GLineEdit_327["fg"] = "#333333"
        GLineEdit_327["justify"] = "center"
        GLineEdit_327["text"] = "Entry"
        GLineEdit_327.place(x=70,y=190,width=70,height=25)

        GLabel_87=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_87["font"] = ft
        GLabel_87["fg"] = "#333333"
        GLabel_87["justify"] = "center"
        GLabel_87["text"] = "Enter number of household utilities "
        GLabel_87.place(x=50,y=250,width=300,height=25)

        GCheckBox_388=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_388["font"] = ft
        GCheckBox_388["fg"] = "#333333"
        GCheckBox_388["justify"] = "center"
        GCheckBox_388["text"] = "Electricity"
        GCheckBox_388.place(x=60,y=300,width=70,height=25)
        GCheckBox_388["offvalue"] = "0"
        GCheckBox_388["onvalue"] = "1"
        GCheckBox_388["command"] = self.GCheckBox_388_command

        GCheckBox_751=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_751["font"] = ft
        GCheckBox_751["fg"] = "#333333"
        GCheckBox_751["justify"] = "center"
        GCheckBox_751["text"] = "Natural Gas"
        GCheckBox_751.place(x=150,y=300,width=90,height=25)
        GCheckBox_751["offvalue"] = "0"
        GCheckBox_751["onvalue"] = "1"
        GCheckBox_751["command"] = self.GCheckBox_751_command

        GCheckBox_887=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_887["font"] = ft
        GCheckBox_887["fg"] = "#333333"
        GCheckBox_887["justify"] = "center"
        GCheckBox_887["text"] = "Oil"
        GCheckBox_887.place(x=350,y=300,width=70,height=25)
        GCheckBox_887["offvalue"] = "0"
        GCheckBox_887["onvalue"] = "1"
        GCheckBox_887["command"] = self.GCheckBox_887_command

        GCheckBox_281=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_281["font"] = ft
        GCheckBox_281["fg"] = "#333333"
        GCheckBox_281["justify"] = "center"
        GCheckBox_281["text"] = "Fuel"
        GCheckBox_281.place(x=260,y=300,width=70,height=25)
        GCheckBox_281["offvalue"] = "0"
        GCheckBox_281["onvalue"] = "1"
        GCheckBox_281["command"] = self.GCheckBox_281_command

        GLabel_64=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_64["font"] = ft
        GLabel_64["fg"] = "#333333"
        GLabel_64["justify"] = "center"
        GLabel_64["text"] = "Total carbon emissions"
        GLabel_64.place(x=50,y=350,width=300,height=25)

        GLineEdit_895=tk.Entry(root)
        GLineEdit_895["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_895["font"] = ft
        GLineEdit_895["fg"] = "#333333"
        GLineEdit_895["justify"] = "center"
        GLineEdit_895["text"] = "Entry"
        GLineEdit_895.place(x=70,y=400,width=70,height=25)

    def GRadio_867_command(self):
        print("command")


    def GRadio_260_command(self):
        print("command")


    def GCheckBox_388_command(self):
        print("command")


    def GCheckBox_751_command(self):
        print("command")


    def GCheckBox_887_command(self):
        print("command")


    def GCheckBox_281_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
