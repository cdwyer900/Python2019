#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:35:09 2018

@author: j2
this creates Text object from nltk
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import csv
import os
import sys


fin = open('CATextpart3.txt','rt')
#fout = open('CAConcordance_likes', 'wt')
#fout.truncate()

text_in = fin.read()

word_tokens = word_tokenize(text_in)
word_tokens.remove('[')
word_tokens.remove(']')
text1 = nltk.Text(word_tokens)


# redirect stdout
#std_out_saved = sys.stdout
#sys.stdout = fout
#text1.concordance('likes', lines=244, width=400)

#put it back
#sys.stdout = std_out_saved

fin.close()
#fout.close()
