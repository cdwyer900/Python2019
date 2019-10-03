#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:46:59 2019

@author: catherineadwyer

do a little more data cleaning

"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import csv
import os
import sys


fin = open('CATextpart3.txt','rt')
fout = open('CATextpart4.txt', 'wt')
fout.truncate()

text_in = fin.read()
""" remove numbers and punc """

import re
text_in2 = re.sub('[0-9]+', '', text_in)
text_in2 = re.sub('-', ' ',text_in2)
text_in2 = text_in2.replace('[','')
text_in2 = text_in2.replace(']','')

stop_words = (' ie if gt ie class','querytype','cssselector',
                 'errorhide', 'lt ', 'lte', 'class','classlte','iemobile'
                 'onerror', 'ie','html','classie','langen',
                 'httpogpmens','dirltr','timeout',
                 'removequery','removequerytype','prefixog',
                 'replacequery', 'replacewith', 'basehref', 
                 'atarget','callbackraw','callback',
                 'atarget','debug','charset','utf',
                 'blank url query','maincontentcol','w','url','urldecode',
                 'xmlnsog','xml','googleon','googleoff','var','div','javalangstring'
                 'rss','languagejavascript','php','sitecatalyst'
                 'pixel','railitem','zflagsz', 'zflagclick',
                 'zflagwidth','zflagsid','zflagcid','javalangstring',
                 'versionhtmlrdfa', 'prefixoghttpogpmens','thu','mar',
                 'integrationapi','bluekai')

""" search for gt using concordance to find words to remove """

text_in3 =  ' '.join([word for word in text_in2.split() if word not in stop_words])



word_tokens = word_tokenize(text_in3)
text1 = nltk.Text(word_tokens)


t_fd = nltk.probability.FreqDist(word_tokens)

fout.write(text_in3)



# redirect stdout
#std_out_saved = sys.stdout
#sys.stdout = fout
#text1.concordance('likes', lines=244, width=400)

#put it back
#sys.stdout = std_out_saved

fin.close()
fout.close()
