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
use nltk to remove junk
"""

fin = open('CAScrubFullTextPart19.txt','rt')
fout = open('CAScrubFullTextPart20.txt', 'wt')
fout.truncate()

text_in = fin.read()


text_in = text_in.replace('rights reserved',' ')
text_in = text_in.replace('debug theme',' ')
text_in = text_in.replace('theme debug',' ')
text_in = text_in.replace('lt-ie9',' ')
text_in = text_in.replace('lt-ie8',' ')
text_in = text_in.replace('no-js',' ')
text_in = text_in.replace('begin output',' ')
text_in = text_in.replace('end output',' ')
text_in = text_in.replace('-w3cdtd xhtml',' ')
text_in = text_in.replace('react-text',' ')


fout.write(text_in)

word_tokens = word_tokenize(text_in)
text = nltk.Text(word_tokens)
 



fin.close()
fout.close()

