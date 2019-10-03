#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:28:10 2018

@author: j2
do stop words and stemming for DOD
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


fin2015 = open('DOD2015.txt','rt')
fin2011 = open('DOD2011.txt', 'rt')
fout2011 = open('DOD2011Stemmed.txt','wt')
fout2015 = open('DOD2015Stemmed.txt','wt')

raw2011 = fin2011.read()
raw2015 = fin2015.read()

raw2011 = raw2011.replace('THIS PAGE INTENTIONALLY LEFT BLANK',' ')
raw2011 = raw2011.replace('STRATEGYFOR','strategy for')
raw2015 = raw2015.replace('THIS PAGE LEFT INTENTIONALLY BLANK',' ')


stop_words = set(stopwords.words('english'))
out2011 = []
out2015 = []

stem2011 = []
stem2015 = []

# remove stop words for files

tokens2011 = word_tokenize(raw2011)
tokens2015 = word_tokenize(raw2015)

for w in tokens2011:
    if w.isalpha() and (w not in stop_words):
        w = w.lower()
        out2011.append(w)

for w in tokens2015:
    if w.isalpha() and (w not in stop_words):
        w = w.lower()
        out2015.append(w)
        
# do stemming
ss = SnowballStemmer("english",ignore_stopwords=True)

for t in out2011:
    tout = ss.stem(t)
    fout2011.write(tout+' ')
    
for t in out2015:
    tout = ss.stem(t)
    fout2015.write(tout+' ')
    
fin2011.close()
fin2015.close()
fout2011.close()
fout2015.close()


        



