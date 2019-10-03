#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:29:20 2018

@author: j2
"""

import string
import collections

from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint


def process_text(text, stem=True):
    """ Tokenize text and stem words removing punctuation """
    #text = text.translate(None, string.punctuation)
    tokens = word_tokenize(text)

    #if stem:
     #   stemmer = PorterStemmer()
      #  tokens = [stemmer.stem(t) for t in tokens]

    return tokens


def cluster_texts(texts, clusters=3):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('english'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)

    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)

    clustering = collections.defaultdict(list)

    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)

    return clustering


# if __name__ == "__main__":
#    articles = [...]  
#clusters = cluster_texts(articles, 7)
#pprint(dict(clusters))
    

#start of program
def start():
    
    fin = open('TargetCorpusFiltered.txt')
    raw = fin.read() 
    print("opened file")
    toks = process_text(raw)
    print(toks)
    clusters = cluster_texts(toks, 7)
    pprint(dict(clusters))
  
start()
