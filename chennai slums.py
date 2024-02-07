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

# the files with the data
list1_1 = pd.read_csv(r"C:\Users\pacha\Downloads\list1_1.csv")
list1_2 = pd.read_csv(r"C:\Users\pacha\Downloads\Screenshot 2024-02-03 215101.png.csv")
#print(list1_1)


house = list1_1[list1_1.columns[[2]]] #no. of households
pop = list1_1[list1_1.columns[[3]]] #population
road = list1_1[list1_1.columns[[5]]] #length of paved road
tap = list1_2[list1_2.columns[[5]]] #no. of tap points/public hydrants installed for supply of protected water
latrines = list1_2[list1_2.columns[[1]]] #no. of private latrines (flush/pour flush)
electricity = list1_2[list1_2.columns[[6]]] #no. of domestic electricity connections


# removing all the missing data in eachof the columns
electricity = electricity.dropna()
latrines = latrines.dropna()
tap = tap.dropna()
road = road.dropna()
#print(pop)
house = house.dropna()
pop = pop.dropna()
#print(house)
#print(pop)


#converting each to dataframe
electricity = pd.DataFrame(electricity)
latrines = pd.DataFrame(latrines)
tap = pd.DataFrame(tap)
house = pd.DataFrame(house)
pop = pd.DataFrame(pop)
road = pd.DataFrame(road)


#joining the population, road and house columns to make a single dataframe
house = house.join(pop, lsuffix="house", rsuffix="pop")
house = house.join(road, lsuffix="house", rsuffix="road")


sno = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

#inserting the same list in all the dataframes and setting it as index
house.insert(0,"newcol", sno)
tap.insert(0,"serial", sno)
tap.set_index("serial")
house.set_index("newcol")
latrines.insert(0,"sl", sno)
electricity.insert(0,"sl", sno)
latrines.set_index("sl")
#print(tap)


# merging the tap, electricity and latrine data in the previously created dataframe
house = house.merge(tap, left_on="newcol", right_on="serial")

house = house.merge(latrines, left_on="newcol", right_on="sl")
house = house.merge(electricity, left_on="newcol", right_on="sl")

# the no. of taps/ no. of houses showing the access households have to tap water
tapperhouse = [(house.loc[:,'17']/house.loc[:,'5'])]




#no of houses relieing on each single tap
housepertap = [(house.loc[:,'5']/house.loc[:,'17'])]

#print(housepertap)

#length of road per household
roadperhouse = [(house.loc[:,"Unnamed: 5"]/house.loc[:,'5'])]


#the average no. of people per household population/households
personperhouse = [(house.loc[:,'6']/house.loc[:,'5'])]

#print(personperhouse)

#print(roadperhouse)

#print(tapperhouse)

#latrines/households since it is given that latrine data is of private latrines, this shows the fraction of households with latrines.
latrinebyhouse =  [(house.loc[:,'13']/house.loc[:,'5'])]



#percentage of households with electric connections
electricbyhouse = [(house.loc[:,'18']/house.loc[:,'5'])*100]

print(electricbyhouse)

#print(latrinebyhouse)








# define function to repeat the steps



























