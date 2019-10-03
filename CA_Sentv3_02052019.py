#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:35:09 2018

@author: j2
TO DO - save compound value plus neg
"""
import re
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment import vader
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from sklearn.model_selection import train_test_split


line_table=[]
key_table = []
key_table_clean = []
results_table = []
neg_table = []
compound_table=[]
vsent = vader.SentimentIntensityAnalyzer()

key_country_table = []
key_country_line = []

#fin = open('CASubSet180317StemmedNGram.txt','rt')
#fin = open('CASubSet180320v2.txt','rt')
fin = open('CATextpart3.txt','rt')
#fout = open('CATextpart2.txt','wt')



for line in fin.readlines():
    print (len(line))
    if len(line)<200:
        print (line)
    else:
        line_table.append(line)



for l in line_table:    
    if len(l)>7:
        print(l[0:7])
        key_table.append(l[0:6])
        results_table.append(vsent.polarity_scores(l))

for tup in results_table:
    neg1, neu2, pos1, com1  = tup.values()
    neg_table.append(neg1)
    compound_table.append(com1)
    
print (np.mean(neg_table))
print (np.max(neg_table))

"""
clean up key table
"""
valid_characters = 'w1234567890'
for key in key_table:
    result = ''.join([ x for x in key if x.lower() in valid_characters ])
    key_table_clean.append(result)

"""

"""




data = pd.read_csv('CAIndexAll.txt',header=None)
for row, line in data.iterrows():
    key_val = str(line[0])
    if key_val in key_table_clean:
        ix = key_table_clean.index(key_val)
        key_country_line.append(line[0])
        key_country_line.append(line[1])
        key_country_line.append(line[2])
        key_country_line.append(line[3])
        key_country_line.append(neg_table[ix])
        key_country_line.append(compound_table[ix])
        key_country_table.append(key_country_line)
        key_country_line=[]
        if neg_table[ix]>.1:
            print (line[0]+ ' '+line[2]+ ' ' + line[3])
            print (results_table[ix])

combine_table = []
combine = []
ix = 0
for key in key_table_clean:
    combine.append(key)
    combine.append(neg_table[ix])
    combine.append(compound_table[ix])
    combine_table.append(combine)
    combine = []
    ix+=1
    
print (np.mean(neg_table))


"""
fin = open('CASubSet180320v2.txt','rt')
raw = fin.read()
word_tokens = word_tokenize(raw)
text = nltk.Text(word_tokens)
"""

import csv

with open('full_results02062019.csv', 'w', newline='') as out_f: # Python 3
    w = csv.writer(out_f, delimiter=',')        # override for tab delimiter
    w.writerows(key_country_table)

        

#use dataframe to sum results by category

     

fin.close()
out_f.close()