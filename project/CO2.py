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
#data = c.fetchall()

c.execute("SELECT Annual_CO2_emissions,year FROM annual WHERE Country= 'New Zealand' ")
data = c.fetchall()


c.execute("SELECT Annual_CO2_emissions,year FROM annual WHERE Country= 'New Zealand' ")
data = c.fetchall()


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


#Carbon footprint calculator of an individual
print("If you are a u are a Non-vegetarian then input 1")
print("Else input any other valid number: ")
carbon_emission=0.0
family_members=float(input("Enter family members: \n"))
food=float(input())
calories=float(input("Enter avg calories: "))

if(food==1):
    carbon_emission += (calories*0.01)*family_members
else:
    carbon_emission += (calories*0.005)*family_members
driven_miles=float(input("Enter avg kms driven in a year: "))
if(driven_miles>0):
    carbon_emission += driven_miles*0.01
else:
    print("enter valid kms driven")
household_utilities=float(input("Enter number of household utilities \nThey include \n 1)Electricity \n2)Natural Gas \n3)Fuel \n4)oil \n"))
total_expenditures=float(input("Enter total expenditures spent after the utilities: "))
if(family_members>0 and household_utilities>0 and total_expenditures>0):
    carbon_emission += (0.12*total_expenditures)*household_utilities
else:
    print("enter valid details: ")
carbon_emission += ((0.12*total_expenditures)*household_utilities)*family_members
print("your carbon emissions in metric tonnes are: ",carbon_emission)






"""
Footprint = 0
class ClimateQuery:
    def __init__(self, question, answer, carbonvalue):
        self.question = question
        self.answer = answer
        self.carbonvalue = carbonvalue
    def mquery(self):
            global Footprint
            loopnum = 0
            mchoice = ['1', '2', '3', '4', '5']
            print('Do you ' + self.question)
            for item in self.answer:
                print(mchoice[0 + loopnum] + ': ' + self.answer[0 + loopnum])
                loopnum = loopnum + 1
            useranswer = input("Choose The Number That Applies to You: ")
            Footprint += self.carbonvalue[int(useranswer) - 1]
            print(' ')
            pass

# qtemplate: q = ClimateQuery('', [''], [])
q_1 = ClimateQuery('commute by', ['Walking', 'Biking', 'Driving', 'Public transit', 'Carpooling'], [0, 0, 1115, 131, 459])
q_2 = ClimateQuery('eat mostly', ['Fast food', 'Home cooked meals'], [4818, 629])
q_3 = ClimateQuery('eat mostly', ['Vegetables/fruit', 'Meat', 'Breads'], [153, 644, 364])
q_4 = ClimateQuery('turn off the lights when you leave a room?', ['Yes', 'No'], [133, 268])
q_5 = ClimateQuery('unplug appliances and chargers when they are not in use?', ['Yes', 'No'], [9, 18])
q_6 = ClimateQuery('dry clothes by', ['Hanging to dry', 'A dryer', 'Both'], [0, 750, 375])
q_7 = ClimateQuery('turn off the water when brushing your teeth?', ['Yes', 'No'], [34, 274])
q_8 = ClimateQuery('turn off the tv after watching it?', ['Yes', 'No'], [47, 140])
q_9 = ClimateQuery('turn off computers while not in use?', ['Yes', 'No'], [29, 90])
q_10 = ClimateQuery('you recycle to the best of your ability?', ['Yes', 'No'], [-150, 20])
qList = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
loop = 0
for element in qList:
    qList[loop].mquery()
    loop = loop + 1
print('Your Carbon Footprint is ' + str(Footprint ) + ' pounds of CO2 a year')
"""