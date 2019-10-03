#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:16:05 2019

@author: catherineadwyer
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv
import gensim
import gensim.corpora as corpora

fin = open('outDict.csv','rt')
tup_list = []

csv_in = csv.reader(fin)

for line in csv_in:
    print (line)
    token = line[0]
    count = int(line[1])
    tup1 = (token)
    tup2 = (tup1, count)
    tup_list.append(tup2)

dd = corpora.Dictionary(tup_list)
text = nltk.Text(tokens)
