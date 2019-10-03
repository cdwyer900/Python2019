#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:59:21 2018

@author: j2
"""

#step 2: remove stop words from file
#remove stopwords from file
#remove urls from file
#remove no-ascii characters
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)



fin = open('TargetCorpusv1.txt','rt')
fout = open('TargetCorpusFiltered.txt','wt')
fstop = open('StopWords_GenericLong.txt','rt')
fdates = open('StopWords_DatesandNumbers.txt','rt')

# remove stopwords
stop_words = set(stopwords.words('english'))
stop_words2 = []
stop_words3 = []

        # read in other stop words file
for sline in fstop.readlines():
    wout = sline.split()
    for w in wout:
        stop_words2.append(w.lower())
        
# remove date stopwords
for dline in fdates.readlines():
    wout = dline.split()
    for w in wout:
        stop_words3.append(w.lower())
        

stop_words.update(set(stop_words2))
stop_words.update(set(stop_words3))



for line in fin.readlines():
    # raw = fin.read()

    # raw = raw.encode('utf-8',errors="replace")
    line = remove_urls(line)
    # print(line)
    
    line2 = re.sub(u'\xc3',' ',line)
    line2 = re.sub(u'\xe2',' ',line2)
    line2 = re.sub(u'\x80',' ',line2)
    line2 = re.sub(u'\xa2',' ',line2)
    line2 = re.sub(u'\xa9',' ',line2)
    line2 = re.sub(u'\xa1',' ',line2)
    line2 = re.sub(u'\x9d',' ',line2)
    line2 = re.sub(u'\x9c',' ',line2)
    
    # filtered_sentence = []
    
    # add in stop words from ND site
    
   # line3 = [w for w in line2 if w.lower() not in stop_words] 
    line3 = ''.join(line2)
    # print(line3)
    
    
    sentence = []
    
    word_tokens = word_tokenize(line3)
    
    for w in word_tokens:
        if w.isalpha() and (w not in stop_words):
            sentence.append(w)
    
    
    text = ' '.join(sentence)
    fout.write(text+"\n")

fin.close
fout.close
fstop.close()
fdates.close()

