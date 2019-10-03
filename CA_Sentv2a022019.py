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
results_table = []
neg_table = []
compound_table=[]
vsent = vader.SentimentIntensityAnalyzer()

key_country_table = []
key_country_line = []

#fin = open('CASubSet180317StemmedNGram.txt','rt')
#fin = open('CASubSet180320v2.txt','rt')
fin = open('CAScrubFullText02042019v2.txt','rt')
fout = open('CATextpart2.txt','wt')
fout.truncate()

text_in = fin.read()
#find the location of each key
#use regular expressions
#m = re.findall("\[w",text_in)
pattern = re.compile("\[w")
replace = ("\n" + "[" + "w")
result=re.sub(pattern,replace,text_in)

result = result.replace('react empty',' ')
result = result.replace('react-empty',' ')
result = result.replace('[if lt ie 9]',' ')
result = result.replace('doctype','')
result = result.replace('[if lte ie 8 ]',' ')
result = result.replace('[if ie 8]',' ')
result = result.replace('[if ie 6]',' ')
result = result.replace('[if lte ie 8]',' ')
result = result.replace('[if ie 8 endif]',' ')
result = result.replace('[if gte ie 9',' ')
result = result.replace('[if ie 7 endif]',' ')
result = result.replace('endif]',' ')
result = result.replace('[if lt ie 7]',' ')
result = result.replace('[if ie 7',' ')
result = result.replace('[if ie 8',' ')
result = result.replace('[if lt ie 10',' ')
result = result.replace('[w8 ','[w8]  ')
result = result.replace('[w4 ','[w4] ')

result = result.replace('[w40 ','[w40] ')

result = result.replace('react-text','')
result = result.replace('lang\"en\"',' ')
result = result.replace('[dynamic posts]','')
result = result.replace('dynamic posts','')
result = result.replace('[custom]', '')
result = result.replace('[if lt ie 7 ','')
result = result.replace('[if lt ie','')
result = result.replace('[if ie','')
result = result.replace('count[4]','')
result = result.replace('  ',' ')
result = result.replace('theme  hook','')
result = result.replace("\'","")
result = result.replace('\"','')

result = result.replace('from from',' ')
result = result.replace('from  ','')
result = result.replace('  ',' ')
result = result.replace('[theme locheader-menu]','')


"""
word_tokens = word_tokenize(result)

ngram_list = nltk.ngrams(word_tokens,40)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)
top_ngrams = ngram_fd.most_common(20)
"""


 



fout.write(result)

fin.close()
fout.close()


"""
need to read in file and break up between keys that begin with [w 


for line in fin.readlines():
    print (len(line))
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



data = pd.read_csv('CAIndexAll.txt',header=None)
for row, line in data.iterrows():
    key_val = '['+ str(line[0])+']'
    if key_val in key_table:
        ix = key_table.index(key_val)
        key_country_line.append(line[0])
        key_country_line.append(line[1])
        key_country_line.append(line[2])
        key_country_line.append(line[3])
        key_country_line.append(neg_table[ix])
        key_country_line.append(compound_table[ix])
        key_country_table.append(key_country_line)
        key_country_line=[]
        if neg_table[ix]>.02:
            print (line[0]+ ' '+line[2]+ ' ' + line[3])
            print (results_table[ix])

combine_table = []
combine = []
ix = 0
for key in key_table:
    combine.append(key)
    combine.append(neg_table[ix])
    combine.append(compound_table[ix])
    combine_table.append(combine)
    combine = []
    ix+=1
    
print (np.mean(neg_table))

fin.close()

fin = open('CASubSet180320v2.txt','rt')
raw = fin.read()
word_tokens = word_tokenize(raw)
text = nltk.Text(word_tokens)

import csv

with open('results031718v2.csv', 'w', newline='') as out_f: # Python 3
    w = csv.writer(out_f, delimiter=',')        # override for tab delimiter
    w.writerows(key_country_table)
"""
    


    
"""
use dataframe to sum results by category

"""       
        





"""
raw = fin.read()
fin2 = open('CASubSet180319v2.txt','rt')
raw2 = fin2.read()
fin3 = open('CASubSet180320v2.txt','rt')
raw3 = fin3.read()


word_tokens = word_tokenize(raw)
word_tokens2 = word_tokenize(raw2)
word_tokens3 = word_tokenize(raw3)


text = nltk.Text(word_tokens)
fd = nltk.FreqDist(text)

results = demo_vader_instance(raw)
results = demo_vader_instance(raw2)
results = demo_vader_instance(raw3)


sentim_analyzer = SentimentAnalyzer()
"""
fin.close()