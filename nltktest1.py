#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:26:33 2018

@author: j2
"""
#   step 1:
#   open file
#   create output file
#   remove html
#   remove stopwords with beautiful soup and
#   re that is regular expression
#   write out to txt file

import nltk
import re

from nltk.corpus import stopwords
from bs4 import BeautifulSoup



#lines = fin.readlines()
soup = BeautifulSoup("<a><b /></a>", "xml")

fin=open('Target201810k.txt')
fout = open('TargetCorpusv1.txt','wt')
text2 = ""

for i in fin.readlines():
    soup = BeautifulSoup(i)
    #text1 = soup.getText()
    #text1 = text1.split()
    #text2 = ' '.join(text1)
    
    text_parts = soup.findAll(text=True)
    text = ' '.join(text_parts)
    
    text2 = re.sub('<[^>]*>',' ',text)
    text2 = re.sub('[[]|[]]',' ',text2)
    text2 = re.sub('[\t\r\f\v]+',' ',text2)
    text2 = re.sub('"',' ',text2)
    # text2 = re.sub('\\',' ',text2)
    text2 = re.sub('\' *\'','',text2)
    text2 = re.sub(', *,',',',text2)
    text2 = re.sub('\?\?+','?',text2)
    text2 = re.sub('\.\.\.\.+','...',text2)
    text2 = re.sub('  +',' ',text2)
    #text2 = re.sub('\n' , ' ', text2)
    text2 = re.sub('  ', ' ', text2)
    text2 = re.sub('  ', ' ', text2)
    text2 = re.sub('  ', ' ', text2)
    text2 = re.sub(u'\xa0', ' ', text2)
    text2 = re.sub(u'\u2013', '2013', text2)
    text2 = re.sub(u'\xa7', ' ', text2)
    text2 = re.sub(u'\u2122', '2122', text2)
    text2 = re.sub(u'\xae', ' ', text2)
    text2 = re.sub(u'\xe2',' ',text2)
    
    text2 = text2.encode('utf-8', errors="replace")   
    # if (text2 != "\n"):
    #    print(text2)
        
    #print(str(text2))
    fout.write(str(text2))
    
fin.close()
fout.close()
    
    

#for line in lines:
#    lineout = soup.getText()
#    print(lineout)
#    fout.write(lineout)
    




#remove html





#tokens = nltk.word_tokenize(raw)
#text = nltk.Text(tokens)

#fout = open('TargetOutputv1.txt','tw')
#fout.write(text)
#fout.close
#fin.close

