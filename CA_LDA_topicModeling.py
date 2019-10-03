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

text_in = fin.read()
     

fin.close()
