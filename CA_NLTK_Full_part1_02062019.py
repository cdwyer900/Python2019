#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:35:09 2018

@author: j2
TO DO - save compound value plus neg
"""
import nltk
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment import vader
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from sklearn.model_selection import train_test_split


fin = open('CATextpart3.txt','rt')
text_in = fin.read()
word_tokens = word_tokenize(text_in)
text2 = nltk.Text(word_tokens)

"""
import sys
sys.stdout = open('CA_collocations.txt', 'w')
text2.collocations(num=300)
"""
text2.concordance_list('facebook')


     

fin.close()
