#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:30:12 2018

@author: j2
get data about index file
"""
import pandas as pd
from pandas import DataFrame


fin = open('CATextv1.txt','rt')
fout = open('CASubSet180323.txt','wt')
fout.truncate()

data = pd.read_csv('CAIndexv1.csv',header=None)
pub_list = []
key_list = []
country_list=[]

for row, line in data.iterrows():
    pub_list.append(line[3])
    country_list.append(line[2])
    if line[1]=='18-03-23':
        key_list.append(line[0])

pub_set = set(pub_list)
country_set = set(country_list)

text = fin.read()

place = 0
tag = '[w'
for key in key_list:
    start = text.find(key,place)
    place = start
    stop = text.find(tag,start)
    print (key)
    print (start)
    print (stop)
    if start == 0:
        out_text = text[start:stop]
    else:
        out_text = text[start-1:stop]
    print (out_text)
    fout.write(out_text+'\n')

fin.close()
fout.close()








