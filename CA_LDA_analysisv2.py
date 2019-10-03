#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:29:55 2018

@author: j2

using nltk to identify topics
and create matrix visualization

"""
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
import numpy as np
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora

fin = open('CAStemmedNGram.txt','rt')
raw = fin.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
pos_corpus = pos_tag(tokens)
# text is an interactive object for use in the console

#fout = open('TargetOutputv1.txt','tw')
#fout.write(text)
#fout.close
fin.close

topics = ["data","breach","secur"]

tokenarray = []
# tokenarray = tokenarray.append(list(tokens))
sentence = []
#create sentences
i=0
for t in tokens:
        sentence.append(t)
        i+=1
       # if i % 20 ==0:
       #     sentence.append("\n")
            
    # print(sentence)
tokenarray.append(list(sentence))

    #make sure each token is unicode

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
d = corpora.Dictionary(tokenarray)

# Converting tokenarray  into  Matrix using dictionary prepared above.
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

text.plot(20)

df.to_csv('out.csv',sep=",")

from contextlib import redirect_stdout

word_fd = nltk.FreqDist(tokens)
mostcommon = word_fd.most_common(10)
plt.barh(range(len(mostcommon)),[val[1] for val in mostcommon], align='center')
plt.yticks(range(len(mostcommon)), [val[0] for val in mostcommon])
plt.show()


with open('helpv2.txt', 'w') as f:
    with redirect_stdout(f):
        print('it now prints to `helpv2.text`')
        text.concordance("breach",lines=25)
        print("co-locations")
        text.collocations(num=30)














