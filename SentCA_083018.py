#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:24:08 2018

@author: j2
clean up key table
"""

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


fin = open('CATextv1.txt','rt')

line_table=[]
key_table = []
results_table = []
length_table = []

neg_table = []
pos_table = []
neu_table = []
compound_table=[]
vsent = vader.SentimentIntensityAnalyzer()



for line in fin.readlines():
    print(line[0:7])
    print (len(line))
    if len(line)>2:
        length_table.append(len(line))
        stop = line.find(']',0)
        key_table.append(line[0:stop+1])
        line_table.append(line)
        results_table.append(vsent.polarity_scores(line))

for tup in results_table:
    neg1, neu2, pos1, com1  = tup.values()
    neg_table.append(neg1)
    neu_table.append(neu2)
    pos_table.append(pos1)
    compound_table.append(com1)

# write out results
sentiment_results_table = []
sentiment_results_line = []

# key, length, neg, neu, pos, compound

for item in key_table:
    i = key_table.index(item)
    sentiment_results_line.append(item[1:len(item)-1])
    sentiment_results_line.append(length_table[i])
    sentiment_results_line.append(neg_table[i])
    sentiment_results_line.append(neu_table[i])
    sentiment_results_line.append(pos_table[i])
    sentiment_results_line.append(compound_table[i])
    sentiment_results_table.append(sentiment_results_line)
    sentiment_results_line = []
    
    
    
    
    
    

with open('sentimentResults083018v1.csv', 'w', newline='') as out_f: # Python 3
    w = csv.writer(out_f, delimiter=',')        # override for tab delimiter
    w.writerows(sentiment_results_table) 
    
fin.close()

        
        
        
    


