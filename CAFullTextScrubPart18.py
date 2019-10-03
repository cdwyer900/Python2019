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
do cleaning for singletons only appear once
"""

fin = open('CAScrubFullTextPart18.txt','rt')
fout = open('CAScrubFullTextPart19.txt', 'wt')
fout.truncate()



text_in = fin.read()


word_tokens = word_tokenize(text_in)
#length of each word
#max length
#average length

max=0
sum=0
count=0
text_out = text_in

for word in word_tokens:
    count+=1
    sum+=len(word)
    if len(word)>max:
        max = len(word)
    if len(word)>15:
        print (word)
        text_out = text_out.replace(word,"")
    #if word_tokens.count(word)==1:
     #   print ("singleton:", word)
        

print ("count: ", count)
avg = sum/count
print ("average: ", avg)
print ("max: ", max)

    
fout.write(text_out)

"""
ngram_list = nltk.ngrams(word_tokens,1)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.least_common(100)

text_out=text_in

for tup in top_ngrams:
    (lst, num) = tup
    out_str=""
    for w in lst:
        out_str=out_str+w+" "
    print (out_str)
    print (num)
    if (num>15):
        text_out = text_out.replace(out_str, " ")
    else:
        print("len 15 or below")
        
        #print (out_str)
        #text_out2 = text_out2.replace(out_str, " ")
text_out = text_out.replace("  ", " ")
fout.write(text_out)
"""

fin.close()
fout.close()

