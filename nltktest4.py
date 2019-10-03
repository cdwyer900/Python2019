#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:15:54 2018

@author: j2
ngram of tokens
creates ngrams
converts top ngrams to
phrases in form of word1_word2

"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# input file of not stemmed tokens
#fin = open('TargetCorpusNotStemmed.txt', 'rt')
fin = open('TargetCorpusStemmed2.txt', 'rt')
fout = open('TargetCorpusWithNgrams.txt','wt')


raw = fin.read()

word_tokens = word_tokenize(raw)
text = nltk.Text(word_tokens)
ngram_list = nltk.ngrams(word_tokens,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)

top_ngrams = ngram_fd.most_common(3000)
sorted_ngrams = sorted(top_ngrams)

firstwords = []
secondwords = []

for row in top_ngrams:
    wordpair, num = row
    one, two = wordpair
    if one != two:
        firstwords.append(one)
        secondwords.append(two)
    
two_words = False
# write out ngrams

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
                if (t == 'data' and word_tokens[i+1] =='breach'):
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







