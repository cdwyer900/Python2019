#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:13:05 2018

@author: j2
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import vader


fin1 = open('CASubSet180317.txt','rt')
fin2 = open('CASubSet180319v2.txt', 'rt')
fin3 = open('CASubSet180320v2.txt','rt')

raw1 = fin1.read()
raw2 = fin2.read()
raw3 = fin3.read()

combined = raw1 + '\n' + raw2 +'\n' + raw3

word_tokens = word_tokenize(combined)
text = nltk.Text(word_tokens)

#Create your bigrams
bgs = nltk.bigrams(word_tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)

ngram_list = nltk.ngrams(word_tokens,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.most_common(200)
sorted_ngrams = sorted(top_ngrams)
import sys
saveout = sys.stdout
sys.stdout = open('output.txt','wt')

text.collocations(200)
sys.stdout = saveout

fin4 = open('output.txt','rt')

fout = open('outputv2.txt','wt')

raw4 = fin4.read()
out1 = raw4.replace('\n',' ')
fout.write(out1)
fout.close()

vsent = vader.SentimentIntensityAnalyzer()
vsent.polarity_scores(combined)

fout2 = open('combined_text.txt','wt')
fout2.write(combined)
fout2.close()




#results2 = demo_liu_hu_lexicon(raw[5000:10000])

