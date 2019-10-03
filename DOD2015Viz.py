#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:13:51 2018

@author: j2
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')



fin2011 = open('DOD2015Stemmed.txt','rt')

raw2011 = []
i=0
for line in fin2011.readlines():
    out = line.split()
    for w in out:
        ll = ''.join(w)
        i+=1
        
        if (i%20==True):
            raw2011.append(ll)


pipeline = Pipeline([('vect',CountVectorizer()),
                     ('tdidf',TfidfTransformer())])

X1 = pipeline.fit_transform(raw2011).todense()

true_k=4
model = KMeans(n_clusters=true_k,max_iter=20000).fit(X1)
ct_vect = pipeline.named_steps['vect']
terms = ct_vect.get_feature_names()

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
for clust in order_centroids:
    print(clust[0:5])

for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind]),
    print



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

centers2D = pca.transform(model.cluster_centers_)


fig2, ax2 = plt.subplots()
fig2.set_figheight(8)
fig2.set_figwidth(8)

    

n=[0,1,2,3]

#ax.scatter(centers2D[:,0], centers2D[:,1], 
 #           marker='x', s=200, linewidths=3, c='r')
#ax.scatter(centers2D[:,0], centers2D[:,1], 
 #           marker='x', linewidths=3, c='r')
ax2.scatter(centers2D[:,0], centers2D[:,1], 
            marker='x', c='r')


for i, txt in enumerate(n):
    ax2.annotate(s=str(txt), xy=centers2D[i],fontsize=14)
                 #not required if using ipython notebook
    
plt.savefig(pp, format='pdf')    

fin.close()
    
