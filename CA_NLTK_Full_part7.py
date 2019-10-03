#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:46:59 2019

@author: catherineadwyer

remove stop words

"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import csv
import os
import sys


fin = open('CATextpart5.txt','rt')
fout = open('CAngramsof2_out_040519.csv','wt')
fout.truncate()

text_in = fin.read()

""" remove stopwords """
stop_words = set (stopwords.words('english'))

#word_tokens = word_tokenize(text_in)
#text1 = nltk.Text(word_tokens)
result_str =  ' '.join([word for word in text_in.split() if word not in stop_words])


word_tokens = word_tokenize(result_str)
text1 = nltk.Text(word_tokens)

ngram_list = nltk.ngrams(word_tokens,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.most_common(500)
sorted_ngrams = sorted(top_ngrams)

out_list = []
out_list2 = []
out_str = ""

for line in top_ngrams:
    ngram, num = line
    print (ngram)
    out_list.append(ngram)
    word1, word2 = ngram
    out_list2.append([word1, word2])


writer = csv.writer(fout)
writer.writerows(out_list2)
     

fin.close()
fout.close()
