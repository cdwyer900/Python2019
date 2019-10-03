#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:41:06 2018

@author: j2
read in from csv file into Pandas dataframe
sum results based on country
compare means

"""
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('results031918.csv')
result1 = df.groupby('country').count()
result2 = df.groupby('country').mean()
result3 = df.groupby('country').mean()
result4 = df.groupby('country').count()

list1 = []
for index, row in result1.iterrows():
    if row['tag_no'] <4:
        list1.append(index)
        #result1=result1.drop(index=index)

for l in list1:
    result1=result1.drop(index=l)      
    result2=result2.drop(index=l)      

df_copy = df

sub1 = result1
sub2 = result2

sub2 = sub2.sort_values(by='neg_result')
result3=result3.sort_values(by='neg_result')

result3.plot(kind='bar',title='Negative Sentiment Results for 03-19-18 (mean, all results)',legend=False)

sub2.plot(kind='bar',title='Negative Sentiment Results for 03-19-18 (mean, n>9)',legend=False)
result4=result4['date']
result4=result4.sort_values()
result4.plot(kind='bar',title='Number Articles Published 03-19-18',legend=False)
