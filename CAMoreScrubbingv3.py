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

def strip_ifs(line, in_x, in_z):
    out_l=line.replace(z, '')
    return out_l
    
CA_stopwords = ['###','##', '--','|','<','>','!!','Google Tag Manager',
                '[if lt IE 9','byline is not empty','doctype']

CA_outText = ""

nltk.download('punkt')

fin = open('CASubSet180323v2.txt','rt')
fout = open('CAScrub180323v2019.txt', 'wt')
fout.truncate()


data = fin.read()
soup1 = BeautifulSoup(data,'html.parser')
text_parts = soup1.findAll(text=True)

text = ' '.join(text_parts)
word_tokens = word_tokenize(text)
text2 = nltk.Text(word_tokens)

ngram_list = nltk.ngrams(word_tokens,10)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)
top_ngrams = ngram_fd.most_common(20)

for t in text2:
    if t not in CA_stopwords:
        CA_outText = CA_outText + t + ' '

for l in CA_outText:
    fout.writelines(l)
    
fin.close()
fout.close()

        

for n in top_ngrams:
    s, count = n
    ss = ''.join(s)
    print (ss)
    
    


print ('stop')


