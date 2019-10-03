#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:33:34 2018

@author: j2

using scikit to do document classification
with tenK file

different type of visualization
use pipeline

does scatterplot visualization on output from
pca stage

does kmeans cluster
displays centers of k clusters on graph
produces list of top n words in each cluster
to add: write cluster terms out to csv file
to add: write pca analysis terms to csv file
to add: lda analysis - topic modeling
to add: text blob library
to add: mds multi-dimensional scaling


"""
import numpy as np

#fin = open('TargetCorpusStemmed2.txt','rt')
fin = open('TargetCorpusWithNgrams.txt','rt')


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
        ll = ''.join(w)
        i+=1
            
        if i%20==0:
            outList.append(ll)
            # print(ll)
            
            
    
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')

import matplotlib.pyplot as plt

pipeline = Pipeline([('vect',CountVectorizer()),
                     ('tdidf',TfidfTransformer())])


#count_vec = CountVectorizer()
#bow = count_vec.fit_transform(raw)

X1 = pipeline.fit_transform(outList).todense()

# principal component analysis
pca = PCA(n_components=2).fit(X1)  # for two dimensions
data2d = pca.transform(X1)

plt.savefig(pp, format='pdf')
plt.autoscale()
plt.scatter(data2d[:,0],data2d[:,1],c='blue')
plt.savefig(pp, format='pdf')
plt.show()

fig1 = plt.figure(figsize = (8,8))
ax1 = fig1.add_subplot(1,1,1) 
ax1.set_xlabel('Principal Component 1', fontsize = 15)
ax1.set_ylabel('Principal Component 2', fontsize = 15)
ax1.set_title('2 component PCA', fontsize = 20)
ax1.scatter(data2d[:,0],data2d[:,1],c='red')

terms = ct_vect.get_feature_names()

for i in range(len(terms)):
    x,y = data2d[i]
    if (x>0.6) or (y>0.6):
        print("x ",x," y ",y," i ",i)
        print(terms[i])




true_k=7
model = KMeans(n_clusters=true_k,max_iter=20000).fit(X1)
ct_vect = pipeline.named_steps['vect']
terms = ct_vect.get_feature_names()

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
for clust in order_centroids:
    print(clust[0:5])

for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print



centers2D = pca.transform(model.cluster_centers_)


fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)

    

n=[0,1,2,3,4,5,6]

#ax.scatter(centers2D[:,0], centers2D[:,1], 
 #           marker='x', s=200, linewidths=3, c='r')
#ax.scatter(centers2D[:,0], centers2D[:,1], 
 #           marker='x', linewidths=3, c='r')
ax.scatter(centers2D[:,0], centers2D[:,1], 
            marker='x', c='r')


for i, txt in enumerate(n):
    ax.annotate(s=str(txt), xy=centers2D[i],fontsize=14)
                 #not required if using ipython notebook
    
plt.savefig(pp, format='pdf')    
    


#bow = np.array(bow.todense())

#words = np.array(count_vec.get_feature_names())
#words[bow[0]>0][:5]

fin.close()
pp.close()


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