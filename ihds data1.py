#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pacha
#
# Created:     08-02-2024
# Copyright:   (c) pacha 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pandas as pd
df = pd.read_stata(r"C:\Users\pacha\Downloads\ICPSR_36151-V6\ICPSR_36151\DS0011\36151-0011-Data.dta")



#print(df.columns)

residence = (df.loc[:,'TH23'])

residence = residence.dropna()

#print(residence)

occupation = df.loc[:,'TH18']

occupation = occupation.dropna()

#print(occupation)

stateid = (df.loc[:, 'STATEID'])


residence = (df.loc[:, 'TH23'])


#converting to dataframe

residence = pd.DataFrame(residence)
stateid = pd.DataFrame(stateid)

#print(residence)

#print(stateid)

#setting the index

rescol = pd.Series(data=residence.index)
statecol = pd.Series(data=stateid.index)

residence.insert(0, "rescol", rescol)

stateid.insert(0, "statecol", statecol)

#print(rescol)

#merging the stateid and residence

stnres = residence.merge(stateid, left_on="rescol", right_on="statecol")


#dropping missing values

stnres = stnres.dropna()

#print(stnres)

same = (stnres.loc[stnres["TH23"] == "Same stae 1"])

#print(same)

#maximum number of people in which category

print(stnres["TH23"].describe())