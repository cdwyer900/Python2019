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


fin = open('CATextpart4.txt','rt')
fout = open('CATextpart5.txt', 'wt')
fout.truncate()

text_in = fin.read()

word_tokens = word_tokenize(text_in)

ngram_list = nltk.ngrams(word_tokens,200)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)
top_ngrams = ngram_fd.most_common(1000)

text_out=text_in

for tup in top_ngrams:
    (lst, num) = tup
    out_str=""
    for w in lst:
        out_str=out_str+w+" "
    #print (out_str)
    if (num>4):
        text_out = text_out.replace(out_str, " ")
    else:
        print("few entries "+num)
        
        #print (out_str)
        #text_out2 = text_out2.replace(out_str, " ")
text_out = text_out.replace("  ", " ")

word_tokens2 = word_tokenize(text_out)
text1 = nltk.Text(word_tokens2)

"""
word_tokens = word_tokenize(text_in)
text1 = nltk.Text(word_tokens)


t_fd1 = nltk.probability.FreqDist(word_tokens)

word_tokens2 = word_tokenize(result_str)
text2 = nltk.Text(word_tokens2)

t_fd2 = nltk.probability.FreqDist(word_tokens2)
"""




# redirect stdout
#std_out_saved = sys.stdout
#sys.stdout = fout
#text1.concordance('likes', lines=244, width=400)

#put it back
#sys.stdout = std_out_saved
fout.write(text_out)

fin.close()
