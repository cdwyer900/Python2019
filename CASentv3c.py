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
from scipy.stats import ttest_ind

df = pd.read_csv('results031703190320v2.csv')
result1 = df.groupby('country').count()
result2 = df.groupby('country').mean()
result3 = df.groupby('date').count()
result4 = df.groupby('date').mean()


"""
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
"""
result2=result2.sort_values(by='neg_result')

result2.plot(kind='bar',title='Negative Sentiment Results by Country ',legend=False)
sub1 = result1['date']
sub1=sub1.sort_values()

sub1.plot(kind='bar',title='Articles Published by Country',legend=False)

sub2 = result3['tag_no']
sub2 = sub2.sort_values()
sub2.plot(kind='bar',title='Articles Published by Date', legend=False)
result4.plot(kind='bar')
cat1=df[df['country']==' US']
cat2 = df[df['country']==' CA']
ttest_ind(cat1['neg_result'],cat2['neg_result'])
cat3=df[df['country']==' GB']
ttest_ind(cat1['neg_result'],cat3['neg_result'])
cat4=df[df['country']==' IN']
ttest_ind(cat1['neg_result'],cat4['neg_result'])
cat5=df[df['country']==' AU']
ttest_ind(cat1['neg_result'],cat5['neg_result'])
cat6=df[df['country']!= ' US']
ttest_ind(cat1['neg_result'],cat6['neg_result'])
cat7=df[df['country']==' IE']
ttest_ind(cat1['neg_result'],cat7['neg_result'])


