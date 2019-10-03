#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:34:39 2019

@author: catherineadwyer
discover ngrams of 2 for stemmed list of tokens

"""
import nltk
from nltk.tokenize import word_tokenize

fin = open('stemmedTokens.txt','rt')

in_str = fin.read()
tokens = word_tokenize(in_str)
text = nltk.Text(tokens)
