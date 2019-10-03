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
    


fin = open('CASubSet180323.txt','rt')
fout = open('CASubSet180323v2.txt','wt')
fout.truncate()

pages = []
x = 0
i = 0
for line in fin.readlines(): 
    #print (line)
    x=0
    while (x!=-1):
        x=line.find('[if',i)
        print (x)
        if x!=-1:
            i=x+1
            y=line.find(']',i)
            print (y)
            if y!=-1:
                z = line[x:y+1]
                print (z)
                line = strip_ifs(line, x, z)
                i=0
                #print (line)
    if line !="":
        fout.write(line)    

fin.close()
fout.close()

fin2 = open('CASubSet180323v2.txt','rt')
fin3 = open('CASubSet180323v3.txt','wt')

data = fin2.read()
soup1 = BeautifulSoup(data,'html.parser')
text_parts = soup1.findAll(text=True)

text = ' '.join(text_parts)
word_tokens = word_tokenize(text)
text2 = nltk.Text(word_tokens)

ngram_list = nltk.ngrams(word_tokens,7)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.most_common(5)

for n in top_ngrams:
    s, count = n
    ss = ''.join(s)
    print (ss)

print ('stop')


