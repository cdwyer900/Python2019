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
part 3 - more data cleaning, remove tag lists

"""

#fin = open('CAScrubFullTextPart2.txt','rt')
#fout = open('CAScrubFullTextPart3.txt', 'wt')
#fout.truncate()
#re-do cleaning 


"""
do cleaning for ngrams of 50
"""

fin = open('CAScrubFullTextPart13.txt','rt')
fout = open('CAScrubFullTextPart14.txt', 'wt')
fout.truncate()



text_in = fin.read()


word_tokens = word_tokenize(text_in)

ngram_list = nltk.ngrams(word_tokens,50)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)
top_ngrams = ngram_fd.most_common(20000)

text_out=text_in

for tup in top_ngrams:
    (lst, num) = tup
    out_str=""
    for w in lst:
        out_str=out_str+w+" "
    print (out_str)
    if (num>4):
        text_out = text_out.replace(out_str, " ")
    else:
        print("one or two entry")
        
        #print (out_str)
        #text_out2 = text_out2.replace(out_str, " ")
text_out = text_out.replace("  ", " ")
fout.write(text_out)


fin.close()
fout.close()

