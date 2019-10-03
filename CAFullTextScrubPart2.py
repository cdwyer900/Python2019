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
part 2 - change to lower case
and remove punctuation

"""

sentence1 = "if asset's byline is not empty show byline otherwise show related author list"
sentence2 = "mobile second level menu starts mobile second level menu ends"
sentence3 = "abcdefghijklmnopqrstuvwxyz"


fout = open('CAScrubFullTextPart2.txt', 'wt')
fout.truncate()

valid_characters = 'abcdefghijklmnopqrstuvwxyz1234567890-[]\'\" '

text_out=""
with open('CAScrubFullTextPart1.txt','rt') as fin:
    for line in fin:
        out_line = line.lower()
        out_line2 = ''.join([ x for x in out_line if x.lower() in valid_characters ])
        out_line2 = out_line2.replace("--","")
        out_line2 = out_line2.replace("  ", " ")
        out_line2 = out_line2.replace(sentence1," ")
        out_line2 = out_line2.replace(sentence2," ")
        out_line2 = out_line2.replace(sentence3, " ")
        
        #print (out_line2)
        text_out=text_out + out_line2 + ' '

    

    



word_tokens = word_tokenize(text_out)

ngram_list = nltk.ngrams(word_tokens,20)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)
top_ngrams = ngram_fd.most_common(10)

text_out2 = text_out

for tup in top_ngrams:
    (lst, num) = tup
    out_str=""
    for w in lst:
        out_str=out_str+w+" "
    print (out_str)
    text_out2 = text_out2.replace(out_str, " ")
        
        #print (out_str)
        #text_out2 = text_out2.replace(out_str, " ")
        



fout.write(text_out2)


"""
for t in token_text:
    if t not in CA_stopwords:
        CA_outText = CA_outText + t + ' '

for l in CA_outText:
    fout.writelines(l)
""" 
"""
for l in text:
    fout.writelines(l)
"""
fin.close()
fout.close()
       
"""
for n in top_ngrams:
    s, count = n
    ss = ''.join(s)
    print (ss)
    
  


print ('stop')
"""

