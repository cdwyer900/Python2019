#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:33:34 2018

@author: j2

using scikit to do document classification
with tenK file
"""
import numpy as np

fin = open('TargetCorpusStemmed2.txt','rt')

# raw = fin.read()
# fin.close()
#fin = open('TargetCorpusFiltered.txt','rt')
# fin = open('TargetCorpusv1.txt','rt')

outList = []
ll = []

i = 0
for l in fin.readlines():
    out = l.split()
    for w in out:
        # print(w)
        if w.isalpha() and len(w)>=3:
            ll = ''.join(w)
            i+=1
            
        if i%20==0:
            outList.append(ll)
            print(ll)
            
            
    
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


#count_vec = CountVectorizer()
#bow = count_vec.fit_transform(raw)

count_vec2 = TfidfVectorizer(stop_words='english')
X = count_vec2.fit_transform(outList)

true_k = 4
model = KMeans(n_clusters=true_k,init='k-means++',max_iter=500,n_init=1)
model.fit(X)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = count_vec2.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

#bow = np.array(bow.todense())

#words = np.array(count_vec.get_feature_names())
#words[bow[0]>0][:5]

fin.close()


"""
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split

X = bow
y = newsgroups.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y)

clf = naive_bayes.GaussianNB().fit(X_train, y_train)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,clf.predict(X_test)))
"""