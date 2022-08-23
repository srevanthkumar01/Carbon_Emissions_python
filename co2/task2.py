import csv
import matplotlib.pyplot as plt

#creating list of dates
x = 1997
dates = []
for i in range(0,14):
    dates.append(x)
    x+=1

#extracting data from csv file to dictionary
data = {}
with open('Emissions.csv') as myFile:
    reader = csv.reader(myFile)
    i=0
    for row in reader:
        if i == 0:
            i += 1
            continue
        l_data=[]
        for i in row:
            try:
                x = float(i)
            except:
                pass
            else:
                l_data.append(x)
        data[(row[0].replace(' ','')).title()]=l_data

print("A Simple Data Analysis Program\n")

print("** Job 1 **\n")
print("All data from Emissions.csv has been read into a dictionary\n")

#
print("** Job 2 **\n")
while(1): 
    year=int(input("Select a year to find the statistics (1997 to 2010):"))
    if year not in dates:
        print("Sorry that is not a valid year.\n")
        continue
    else:
        country_list = []
        data_list = []
        position=dates.index(year)
        for i in data:
            country_list.append((i.replace(' ','')).title())
            data_list.append((data[i])[position])
        print('\nIn {} countris with minimum and maximum CO2 emission levels were: [{}] and [{}] respectively'.format(year,country_list[data_list.index(min(data_list))],country_list[data_list.index(max(data_list))]))
        print('\nAverage CO2 emissions in {} were {}\n'.format(year,round(sum(data_list)/len(data_list),6)))
        break

#Creating subset of the given data
print("** Job 3 **\n")
while(1):
    flag=0
    names=input("Write up to three comma-separated countries for which you want to extract data:")
    country_names=names.split(',')
    if len(country_names)>3:
        print('ERR: Sorry, at most 3 countries can be entered.')
        continue
    for i in country_names:
        if (i.replace(' ','')).title() not in country_list:
            print('ERR: Sorry "{}" is not a valid country'.format(i))
            break
        else:
          flag=1  

    if flag==0:
        continue

    else:
        subset_list=[]
        try:
            myFile = open('subset.csv','r')
        except FileNotFoundError:
            myFile = open('subset.csv','w')
            header=dates.copy()
            header.insert(0,'CO2 per capita')
            subset_list.append(header)
            with myFile:
                writer = csv.writer(myFile)
                for i in country_names:
                    temp=[]
                    temp.append(i.replace(' ','').title())
                    for j in data[(i.replace(' ','')).title()]:
                        temp.append(j)
                    subset_list.append(temp)
                writer.writerows(subset_list)
        else:
            myFile = open('subset.csv','a')
            with myFile:
                writer = csv.writer(myFile)
                for i in country_names:
                    temp=[]
                    temp.append(i.replace(' ','').title())
                    for j in data[(i.replace(' ','')).title()]:
                        temp.append(j)
                    subset_list.append(temp)
                writer.writerows(subset_list)
        break

#Emission Plot uding matplotlib
print("** Job 4 **\n")
name=input('Select the country to visualize:')
emission = data[(name.replace(' ','')).title()]
#hist,scatter,plot
plt.plot(dates,emission,marker='o')
plt.title('Emissions Plot for {}'.format((name.replace(' ','')).title()))
plt.xlabel('Year')
plt.ylabel('CO2 emissions')
plt.show()


            
    
    

