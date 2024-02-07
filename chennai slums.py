#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pacha
#
# Created:     02-02-2024
# Copyright:   (c) pacha 2024
# Licence:     <your licence>
#------------------------------------------------------------------------------
import pandas as pd
import numpy as np
list1_1 = pd.read_csv(r"C:\Users\pacha\Downloads\list1_1.csv")
list1_2 = pd.read_csv(r"C:\Users\pacha\Downloads\Screenshot 2024-02-03 215101.png.csv")
#print(list1_1)
house = list1_1[list1_1.columns[[2]]]
pop = list1_1[list1_1.columns[[3]]]
road = list1_1[list1_1.columns[[5]]]
tap = list1_2[list1_2.columns[[5]]]
latrines = list1_2[list1_2.columns[[1]]]
electricity = list1_2[list1_2.columns[[6]]]


electricity = electricity.dropna()
latrines = latrines.dropna()
tap = tap.dropna()
road = road.dropna()
#print(pop)
house = house.dropna()
pop = pop.dropna()
#print(house)
#print(pop)

electricity = pd.DataFrame(electricity)
latrines = pd.DataFrame(latrines)
tap = pd.DataFrame(tap)
house = pd.DataFrame(house)
pop = pd.DataFrame(pop)
road = pd.DataFrame(road)
house = house.join(pop, lsuffix="house", rsuffix="pop")
house = house.join(road, lsuffix="house", rsuffix="road")

sno = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]


house.insert(0,"newcol", sno)
tap.insert(0,"serial", sno)
tap.set_index("serial")
house.set_index("newcol")
latrines.insert(0,"sl", sno)
electricity.insert(0,"sl", sno)
#print(tap)
house = house.merge(tap, left_on="newcol", right_on="serial")

latrines.set_index("sl")

house = house.merge(latrines, left_on="newcol", right_on="sl")

#tapperhouse = [(house.loc[:,'17']/house.loc[:,'6'])]

house = house.merge(electricity, left_on="newcol", right_on="sl")

#print(house)

#no of houses relieing on each single tap
housepertap = [(house.loc[:,'5']/house.loc[:,'17'])]

#print(housepertap)

roadperhouse = [(house.loc[:,"Unnamed: 5"]/house.loc[:,'5'])]

personperhouse = [(house.loc[:,'6']/house.loc[:,'5'])]

#print(personperhouse)

#print(roadperhouse)

#print(tapperhouse)

latrinebyhouse =  [(house.loc[:,'13']/house.loc[:,'5'])]

electricbyhouse = [(house.loc[:,'18']/house.loc[:,'5'])*100]
#percentage of households with electric connections

print(electricbyhouse)

#print(latrinebyhouse)








# define function to repeat the steps



























