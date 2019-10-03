#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: j2
stemming on unigrams
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *



fin = open('CAUniGramOut.txt','rt')
fout = open('outDict.csv','wt')

raw = fin.read()
stemmed = ""


tokens = word_tokenize(raw)
stemmer = PorterStemmer()

for t in tokens:
    word = stemmer.stem(t)
    stemmed = stemmed + word + ' '
        

tokens2 = word_tokenize(stemmed)
ngram_fd = nltk.probability.FreqDist(tokens2)

top_ngrams = ngram_fd.most_common(5000)
d = dict(top_ngrams)

import csv
 
#need to fix this csv not working
csv_out = csv.writer(fout, delimiter=',')
for key, val in d.items():
    csv_out.writerow([key, val])


#get rid of tokens that only appear a few times
# take output and save to gensim dictionary for additional analysis

# Gensim


fin.close()
fout.close()

import gensim
import gensim.corpora as corpora

tokenarray=[]


tokenarray.append(tokens2)

    #make sure each token is unicode

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
d = corpora.Dictionary(tokenarray)
dd = dict(top_ngrams)

# Converting tokenarray  into  Matrix using dictionary prepared above.
#need to fix this

doc_term_matrix = [d.doc2bow(doc) for doc in tokenarray]
Lda = gensim.models.ldamodel.LdaModel

ldamodel = Lda(doc_term_matrix, num_topics=5,id2word=d,passes=100)

for i in  ldamodel.show_topics(num_words=4):
    # a = i[1].split('*')
    print (i[0], i[1])
    
K = ldamodel.num_topics
topicWordProbMat = ldamodel.print_topics(K,5)
print("matrix")
print (topicWordProbMat) 

print("vector")
for t in tokenarray:
     vec = d.doc2bow(t)
     print (ldamodel[vec])

# import pandas as pd
# import numpy as np
import numpy as np
import pandas as pd
from pprint import pprint

columns = ['1','2','3','4','5','6','7']
df = pd.DataFrame(columns = columns)
pd.set_option('display.width', 1000)

# 40 will be resized later to match number of words in DC
zz = np.zeros(shape=(25,K))

last_number=0
DC={}

for x in range (10):
  data = pd.DataFrame({columns[0]:"",
                     columns[1]:"",
                     columns[2]:"",
                     columns[3]:"",
                     columns[4]:"",
                     columns[5]:"",
                     columns[6]:"",
                    },index=[0])
  df=df.append(data,ignore_index=True)  

for line in topicWordProbMat:

    tp, w = line
    probs=w.split("+")
    y=0
    for pr in probs:
               
        a=pr.split("*")
        df.iloc[y,tp] = a[1]
       
        if a[1] in DC:
           zz[DC[a[1]]][tp]=a[0]
        else:
           zz[last_number][tp]=a[0]
           DC[a[1]]=last_number
           last_number=last_number+1
        y=y+1
print ("df")
print (df)
print("zz")
print (zz)

import matplotlib.pyplot as plt
zz=np.resize(zz,(len(DC.keys()),zz.shape[1]))

for val, key in enumerate(DC.keys()):
        plt.text(-2.5, val + 0.5, key,
                 horizontalalignment='center',
                 verticalalignment='center'
                 )
plt.imshow(zz, cmap='cool', interpolation='nearest',aspect='auto')
plt.show()

#write out tokens2 stemmed tokens
fout2 = open('stemmedTokens.txt','wt')
fout2.truncate()
out_str = ' '.join(tokens2)
out_str = out_str+'\n'

fout2.write(out_str)
fout2.close()

        



