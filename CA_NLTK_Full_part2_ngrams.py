#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:35:09 2018

@author: j2
TO DO - save compound value plus neg
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import csv


fin = open('CATextpart3.txt','rt')
fout = open('CAngramsof4_out.csv','wt')
fout.truncate()

text_in = fin.read()

""" remove stopwords """
stop_words = set (stopwords.words('english'))
stop_words.add('[')
stop_words.add(']')

#word_tokens = word_tokenize(text_in)
#text1 = nltk.Text(word_tokens)
result_str =  ' '.join([word for word in text_in.split() if word not in stop_words])


word_tokens = word_tokenize(result_str)
word_tokens.remove('[')
word_tokens.remove(']')
text1 = nltk.Text(word_tokens)

ngram_list = nltk.ngrams(word_tokens,4)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.most_common(500)
sorted_ngrams = sorted(top_ngrams)

out_list = []
out_list2 = []
out_str = ""

for line in top_ngrams:
    ngram, num = line
    print (ngram)
    out_list.append(ngram)
    word1, word2, word3, word4 = ngram
    out_list2.append([word1, word2, word3, word4])


writer = csv.writer(fout)
writer.writerows(out_list2)
     

fin.close()
fout.close()
