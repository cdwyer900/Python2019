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

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')

"""
https://stackoverflow.com/questions/12488722/counting-bigrams-pair-of-two-words-in-a-file-using-python/12488794#12488794
"""

outCA = []
stemCA = ""

finCA = open('CATextpart5.txt','rt')
raw = finCA.read()

stop_words = set(stopwords.words('english'))

tokens = word_tokenize(raw)
tokensv2 = [w for w in tokens if not w in stop_words]

ngram_generator = nltk.ngrams(tokensv2,1)
ngram_fd = nltk.probability.FreqDist(ngram_generator)
t_fd = nltk.probability.FreqDist(tokens)

top_ngrams = ngram_fd.most_common()
sorted_ngrams = sorted(top_ngrams)

tokensv3 = []
for token_tuple in top_ngrams:
    #print (token_tuple)
    out_token, num = token_tuple
    #print (out_token)
    if num >3:
        tokensv3.append(out_token)

ss = SnowballStemmer("english",ignore_stopwords=True)

tt = ""
for t in tokensv3:
    tt = ''.join(t)
    tout = ss.stem(tt)
    
    stemCA = stemCA + tout + ' '
    #print (tout)

tokens_stem = word_tokenize(stemCA)
ngram_generator_stem = nltk.ngrams(tokens_stem,1)
ngram_fd_stem = nltk.probability.FreqDist(ngram_generator_stem)
t_fd_stem = nltk.probability.FreqDist(tokens_stem)

top_ngrams_stem = ngram_fd_stem.most_common()
sorted_ngrams_stem = sorted(top_ngrams_stem)

tokensv4 = []

for token_tuple in top_ngrams_stem:
    out_token, num = token_tuple
    tt = ''.join(out_token)
    tokensv4.append(tt)

tokenarray.append(list(tokensv4))

    #make sure each token is unicode

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
d = corpora.Dictionary(tokenarray)

# Converting tokenarray  into  Matrix using dictionary prepared above.
doc_term_matrix = [d.doc2bow(doc) for doc in tokenarray]
Lda = gensim.models.ldamodel.LdaModel

ldamodel = Lda(doc_term_matrix, num_topics=3,id2word=d,passes=1000)

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





"""
rawCA = []
i=0
for line in finCA.readlines():
    out = line.split()
    for w in out:
        ll = ''.join(w)
        i+=1
        
        if (i%20==True):
            rawCA.append(ll)


pipeline = Pipeline([('vect',CountVectorizer()),
                     ('tdidf',TfidfTransformer())])

X1 = pipeline.fit_transform(rawCA).todense()

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
"""
pp.close()
    
