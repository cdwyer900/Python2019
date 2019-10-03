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

df = pd.read_csv('results032018.csv')
result1 = df.groupby('country').count()
result2 = df.groupby('country').mean()
result3 = df.groupby('country').mean()

list1 = []
for index, row in result1.iterrows():
    if row['tag_no'] <9:
        list1.append(index)
        #result1=result1.drop(index=index)

for l in list1:
    #result1=result1.drop(index=l)      
    result2=result2.drop(index=l)      

df_copy = df

sub1 = result1
sub2 = result2

sub2 = sub2.sort_values(by='neg_result')
result3=result3.sort_values(by='neg_result')

result3.plot(kind='bar',title='Negative Sentiment Results for 03-20-18 (mean, all results)',legend=False)

sub2.plot(kind='bar',title='Negative Sentiment Results for 03-20-18 (mean, n>9)',legend=False)
sub3=sub1['date']
sub3=sub3.sort_values()
sub3.plot(kind='bar',title='Number Articles Published 03-20-18',legend=False)
