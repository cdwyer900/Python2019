#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:33:34 2018

@author: j2

using scikit to do document classification
lda topic modeling
"""
import numpy as np
from sklearn.datasets import fetch_20newsgroups
categories=["rec.autos","rec.motorcycles"]

newsgroups = fetch_20newsgroups(categories=categories)

from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()
bow = count_vec.fit_transform(newsgroups.data)

bow = np.array(bow.todense())

words = np.array(count_vec.get_feature_names())
words[bow[0]>0][:5]

from sklearn import naive_bayes
from sklearn.model_selection import train_test_split

X = bow
y = newsgroups.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y)

clf = naive_bayes.GaussianNB().fit(X_train, y_train)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,clf.predict(X_test)))