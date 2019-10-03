#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 10 2018

@author: j2
do stop words and stemming for CA - text case
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


fin = open('CATextpart5.txt','rt')
fout = open('CAStemmedNGramv2.txt','wt')
fout.truncate()

raw = fin.read()

stop_words = set(stopwords.words('english'))
outCA = []
stemCA = ""
CA_stopwords = ['the','it','said','and','one','in','say','could','also',
                'say','told','sat mar', 'last modifi','doctype']

# remove stop words for files

tokens = word_tokenize(raw)

for w in tokens:
    w = w.lower()
    if w.isalpha() and (w not in stop_words)and (w not in CA_stopwords):
        #print (w)
        outCA.append(w)
        
# do stemming
ss = SnowballStemmer("english",ignore_stopwords=True)

for t in outCA:
    tout = ss.stem(t)
    stemCA = stemCA + tout + ' '
    #print (tout)

#do ngrams
firstwords = []
secondwords = []
two_words = False

word_tokens = word_tokenize(stemCA)
ngram_list = nltk.ngrams(word_tokens,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)

top_ngrams = ngram_fd.most_common(200)
sorted_ngrams = sorted(top_ngrams)

for row in sorted_ngrams:
    wordpair, num = row
    one, two = wordpair
    if one != two:
        firstwords.append(one)
        secondwords.append(two)

for i in range(len(word_tokens)):
    if two_words: #skip this time because previous ngram has word
        two_words = False
       # print("continue")
       # print(i)
    else:
        # begin else
        t = word_tokens[i]
        # print(t)
        if t not in firstwords:
            fout.write(t+' ')
        else:
            inx = firstwords.index(t)
            # now this value is i inx2 = word_tokens.index(t)
            # check to see if we are at the end
            if (i+1) >=len(word_tokens):
                fout.write(t+' ')
            else:
                two_words = True
                if (t == 'cambridg' and word_tokens[i+1] =='analytica'):
                        phras = str(t+'_'+word_tokens[i+1])
                        fout.write(phras+' ')
                else:
                    if (secondwords[inx] == word_tokens[i+1]):
                        phras = str(t+'_'+word_tokens[i+1])
                        fout.write(phras+' ')
                    else:
                        fout.write(t+' ')

    
fin.close()
fout.close()


        



