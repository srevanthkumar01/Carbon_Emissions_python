import matplotlib.pyplot as plt
import sqlite3
import numpy as np

def CO2Emissions():
    conn = sqlite3.connect('C:\\Users\\revwr\\Downloads\\Sqlite databases\\rev1.db')
    c = conn.cursor()

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

    # def graph_data():
    # c.execute('SELECT Annual_CO2_emissions,year FROM annual')
    # data = c.fetchall()

    c.execute("SELECT Annual_CO2_emissions,year FROM annual WHERE Country='France'" )
    data = c.fetchall()

    year = []
    emission = []
    country = []

    for row in data:
        # country.append(row[0])
        year.append(row[0])
        emission.append(row[1])

    print("Country = ", country)
    print("Year = ", year)
    print("CO2 emission = ", emission)

    plt.plot(emission, year)
    plt.ylim()
    plt.xlabel("Years")
    plt.ylabel("CO2 emissions")
    plt.title("Annual CO2 Emission")

    plt.show()
