#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:48:27 2019

@author: catherineadwyer
"""

"""
read in an excel file into a panda dataframe
"""
import numpy as np
import pandas as pd
import pycountry


xl = pd.ExcelFile("PeaceIndex2017.xlsx")
df = xl.parse("Sheet1")

"""
check country names from peace index file, compare to official name
"""
cList = df['Country'].tolist()
#list from peace index
cList2 = []
#names from pycountry
pycList=[]
    
for item in cList:
    str1 = item
    str1 = str1.lstrip()
    cList2.append(str1)

#relace column in dataframe with cleaned names in cList2
n = df.columns[0]
df.drop(n, axis=1, inplace = True)
df[n]=cList2

for country in pycountry.countries:
    #print(country)
    if country.name in cList2:
        #print(country.name)
        pycList.append(country.name)
    else:
        print("not in list: " + country.name)

print("Peace Index Names not in Country List")
for country in cList2:
    if country not in pycList:
        print(country)

xl2 = pd.ExcelFile("countryListTargeted.xlsx")
df2 = xl2.parse("countryListTargeted")
dataList = df2['Country'].tolist()

print("dataset names not in peace index list")
for country in dataList:
    if country not in cList2:
        print(country)

# update names in peace index dataframe
df2.replace("US","United States",inplace=True)
df2.replace("North Korea","DPR Korea",inplace=True)
df2.replace("South Korea","Korea Republic",inplace=True)

df_joined = df2.set_index('Country').join(df.set_index('Country'),how='inner') 
df_joined_outer = df2.set_index('Country').join(df.set_index('Country'),how='outer') 
df_joined_outer['Mentions'].fillna(0,inplace=True)

df_joined.to_excel("output_result.xlsx")   
df_joined_outer.to_excel("full_peace_index_results.xlsx")




