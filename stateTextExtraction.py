#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:57:10 2019

@author: catherineadwyer
"""
import pycountry
import string
import operator
"""
set up separate input for target data versus attacker data
"""

fin=open('StateCountriesTargeted.txt', 'rt')
fout = open('countryListTargeted.txt', 'wt')
fout.truncate()

fin2=open('StateCountriesAttackers.txt', 'rt')
fout2 = open('countryListAttackers.txt', 'wt')
fout2.truncate()


in_str = fin.read()
in_str2 = fin2.read()
in_str2 = in_str2.replace('SS-','')
#remove numbers and punctuation
exclude=set(string.punctuation)
exclude=exclude.union(set(string.digits))

str2 = ''.join(ch for ch in in_str if ch not in exclude)
str3 = ''.join(ch for ch in in_str2 if ch not in exclude)
#add code to exclude stopwords

moreCountries = ["Russia","US","South Korea","North Korea","Iran","Vietnam","Czech Republic","Unknown"]
#common name of country is different than official name
#countryList is the list of countries mentioned once per country
#cleanedList is all mentions of any country
#summaryList is country names plus count of mentions
countryTargetList = []
countTargetList = []
countryAttackList = []
countAttackList = []


for country in pycountry.countries:
    #print(country)
    if country.name in in_str:
        #print(country.name)
        countryTargetList.append(country.name)
    if country.name in in_str2:
        countryAttackList.append(country.name)

for cName in moreCountries:
    if cName in in_str and cName !="Unknown":
        #print(cName)
        countryTargetList.append(cName)
    if cName in in_str2:
        countryAttackList.append(cName)

#create string with just country names in it

for country in countryTargetList:
    print(country)
    if country in in_str:
        key=country
        value=in_str.count(country)
        item=(key,value)
        countTargetList.append(item)


sortedCountryTargetList = sorted(countTargetList, key=operator.itemgetter(1),reverse=True)

for item in sortedCountryTargetList:
    #print(item)
    #fout.writelines(item)
    val1 = item[0]
    val2 = item[1]
    line = val1 + ", " + str(val2)+"\n"
    fout.write(line)

for country in countryAttackList:
    if country in in_str2:
        key=country
        value=in_str2.count(country)
        item=(key,value)
        countAttackList.append(item)

sortedCountryAttackList = sorted(countAttackList, key=operator.itemgetter(1),reverse=True)
for item in sortedCountryAttackList:
    #print(item)
    #fout.writelines(item)
    val1 = item[0]
    val2 = item[1]
    line = val1 + ", " + str(val2)+"\n"
    fout2.write(line)




fin.close()
fout.close()
fin2.close()
fout2.close()
