#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 18:29:48 2018

@author: j2
"""
from bs4 import BeautifulSoup, Comment
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords

"""
nltk analysis of full text
"""

fin = open('CAtextpart2.txt','rt')
fout = open('CAtextpart3.txt','wt')
fout.truncate



text_in = fin.read()


word_tokens = word_tokenize(text_in)
text = nltk.Text(word_tokens)

V = set(text)
long_words = [w for w in V if len(w)>20]

for word in long_words:
    text_in = text_in.replace(word,'')

fout.write(text_in)

fin.close()
fout.close()

