#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:15:55 2018

@author: j2

use scikit to do clustering and distance modeling
"""
import numpy as np
import pandas as pd

from sklearn.datasets import make_blobs

blobs,classes = make_blobs(500, centers=3)

import matplotlib.pyplot as plt
# %matplotlib inline
f, ax = plt.subplots(figsize=(7.5,7.5))
rgb = np.array(['r','g','b'])
ax.scatter(blobs[:,0],blobs[:,1],color=rgb[classes])
ax.set_title("Blobs")

from sklearn.cluster import KMeans
kmean = (KMeans(n_clusters=3))

kmean.fit(blobs)

"""
KMeans(algorithm='auto',copy_x=True,init='k-means++',max_iter=300,
       n_clusters=3,n_init=10,n_jobs=1,
       precompute_distances='auto',random_state=None,
       tol=0.0001,verbose=0)
kmean.cluster_centers_ 
array([[3.4839154,-0.92786786],[-2.05114953,1.58697731],
                             [1.58182736,-6.80678064]])
"""
f, ax = plt.subplots(figsize=(7.5,7.5))
ax.scatter(blobs[:,0],blobs[:,1],color=rgb[classes])
ax.scatter(kmean.cluster_centers_[:,0],kmean.cluster_centers_[:,1],
           marker='*',s=250,
           color='black',label='Centers')
ax.set_title('Blobs')
ax.legend('Best')



# fin=open('TargetCorpusStemmed2.txt','rt')



