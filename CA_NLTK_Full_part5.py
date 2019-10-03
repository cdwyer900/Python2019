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

text_in = fin.read()

"""remove stopwords """
stop_words = set (stopwords.words('english'))

#word_tokens = word_tokenize(text_in)
#text1 = nltk.Text(word_tokens)
result_str =  ' '.join([word for word in text_in.split() if word not in stop_words])



word_tokens = word_tokenize(text_in)
text1 = nltk.Text(word_tokens)


t_fd1 = nltk.probability.FreqDist(word_tokens)

word_tokens2 = word_tokenize(result_str)
text2 = nltk.Text(word_tokens2)

t_fd2 = nltk.probability.FreqDist(word_tokens2)





# redirect stdout
#std_out_saved = sys.stdout
#sys.stdout = fout
#text1.concordance('likes', lines=244, width=400)

#put it back
#sys.stdout = std_out_saved

fin.close()
