#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:52:37 2018

@author: j2
shrink down the index and remove duplicate entries
"""

import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup, Comment
import requests
import re
import bleach
import numpy.random
import sys

def clean_page(in_page):
    soup1 = BeautifulSoup(in_page,'html.parser')
    [x.decompose() for x in soup1.find_all('script')]
    [x.decompose() for x in soup1.find_all('style')]
    [x.decompose() for x in soup1.find_all('meta')]
    [x.decompose() for x in soup1.find_all('noscript')]  
    [x.decompose() for x in soup1.find_all('span')]
    [x.decompose() for x in soup1.find_all('li')]
    [x.decompose() for x in soup1.find_all('a')]
    
    
    for s in soup1(['script','style']):
        s.decompose()
        
    text_parts = soup1.findAll(text=True)

    text = ' '.join(text_parts)


    text2 = re.sub('\n', ' ', text)
    text2 = re.sub('html','',text2)
    text2 = re.sub('  ', ' ', text2)
    text2 = re.sub('  ', ' ', text2)
    p = re.compile(r'data-uri="[\w*\.\/\@-]*\"')

    for match in p.findall(text2):
        text2 = text2.replace(match, '')
        
    p2 = re.compile(r'\[if[ \w\.\=\<\>\:\;\"\/\]\(\)!\|]*?!\[endif\]')
    
    for match2 in p2.findall(text2):
        text2 = text2.replace(match2,'')
        #print(text2)
    return text2

# begin main
fin2 = open('CAContentOutAll.txt','rt')
fout1 = open('CAIndexv1.txt','wt')
fout2 = open('CATextv1.txt','wt')

fout1.truncate()
fout2.truncate()

# input into a NumPy array
data = pd.read_csv('CAIndexAll.txt',header=None)

data_compressed = data.drop_duplicates(subset=4)
data_compressed = data_compressed[:2777]

contents = ""
contents = fin2.read()
   
key_table=[]
text_table = []
out_text = ""
tag = '[w'

for row, line in data_compressed.iterrows():
    key_table.append(line[0])

place = 0
for key in key_table:
    start = contents.find(key,place)
    place = start
    stop = contents.find(tag,start)
    #print (start)
    #print (stop)
    if start == 0:
        out_text = contents[start:stop]
    else:
        out_text = contents[start-1:stop]

    text_entry = out_text
    text_table.append(text_entry)

for i in range(len(text_table)):
    text_table[i]=clean_page(text_table[i])
    fout2.write(text_table[i])
    if len(text_table[i])>9000:
        print (i)
    #print (len(text_table[i]))
    fout2.write('\n\n')

data_compressed.to_csv('CAIndexv1.csv',index_label=False,index=False,header=False)




fin2.close()
fout1.close()
fout2.close()


    
    

    

    


        
    


