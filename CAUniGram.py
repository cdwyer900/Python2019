#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 10 2018

@author: j2
do stop words and stemming for CA - text case
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


fin = open('CATextpart5.txt','rt')
fout = open('CAUniGramOut.txt','wt')
fout.truncate()

raw = fin.read()

stop_words = set(stopwords.words('english'))
outCA = ""
stemCA = ""

tokens = word_tokenize(raw)

for w in tokens:
    w = w.lower()
    if (w.isalpha() and (w not in stop_words)):
        outCA = outCA + w + ' '
        #print (w)    

        
"""
# do stemming
ss = SnowballStemmer("english",ignore_stopwords=True)

for t in outCA:
    tout = ss.stem(t)
    stemCA = stemCA + tout + ' '
    #print (tout)


word_tokens = word_tokenize(stemCA)
ngram_list = nltk.ngrams(word_tokens,1)
ngram_fd = nltk.probability.FreqDist(ngram_list)

top_ngrams = ngram_fd.most_common()
sorted_ngrams = sorted(top_ngrams)

"""

fin.close()
fout.close()


        



