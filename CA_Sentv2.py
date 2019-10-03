#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:35:09 2018

@author: j2
"""
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment import vader
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from sklearn.model_selection import train_test_split
sentence = "Cambridge Analytica: Firm Courted By BJP, Congress (and Trump) In Trouble Over Data Breach Cambridge Analytica: Firm Courted By BJP, Congress (and Trump) In Trouble Over Data Breach Most of us in India know of Cambridge Analytica as the big data analytics firm that is reportedly being courted by both the BJP and the Congress in the run up to the 2019 Lok Sabha elections. The world over, the firm is famous -- or rather infamous -- for its role in Donald Trump’s ascension to the White House and its links to the Brexit Leave campaign in the United Kingdom. What the firm essentially does is use big data to help clients track preferences and thereby formulate strategies. Sounds simple enough till your begin to realise just exactly what this data is comprised of. A whistleblower recently revealed that Cambridge Analytica harvested millions of Facebook profiles of US voters and used the data to build a powerful software program to predict and influence voting choices. The firm built the system in early 2014, profiling individual voters and then using the information to target them with personalised political advertisements. The programme affected 50 million people, who never knew that their data had been taken. The data was used to construct complex psychological profiles of voters, who were then targeted with political ads that were designed to subtly motivate them to vote a particular way. Christopher Wylie, who worked with a Cambridge University academic to obtain the data, told the Observer: “We exploited Facebook to harvest millions of people’s profiles. And built models to exploit what we knew about them and target their inner demons. That was the basis the entire company was built on.” It turns out that Facebook knew that this was going on. Documents show that by 2015 Facebook was well aware that information had been harvested on an unprecedented scale. Yet, it failed to alert users or take steps to recover and secure the information. Cambridge Analytica was headed at the time by Trump’s key adviser Steve Bannon. Data was collected through an app built by academic Aleksandr Kogan’s company Global Science Research (GSR). In collaboration with Cambridge Analytica, hundreds of thousands of users were paid to take a personality test and agreed to have their data collected for academic use. The app then collected the data of test taker’s pool of Facebook friends, going on to build a massive database. The story that Cambridge Analytica collected private information and used it to influence voting behaviour at the US elections comes as both Cambridge Analytica and Facebook are one focus of an inquiry into data and politics by the British Information Commissioner’s Office. Separately, the Electoral Commission is also investigating what role Cambridge Analytica played in the EU referendum. Facebook has sought damage control by announcing that it was suspending Cambridge Analytica from the platform, but the fact that this suspension comes a few years after Facebook knew of the firm’s activities in harvesting data does little to mitigate its reputation. At the end of the day, questions remain about Facebook’s role in influencing electoral results. Interestingly, Cambridge Analytica and the tools it uses seem to be in hot demand in South Asia. The BJP and Congress have both reportedly considered the firm, as has former Sri Lankan President Mahinda Rajapaksa and Bangladesh’s Awami League. The firm seems to have worked with Indian political parties. On its website, it says: “CA was contracted to undertake an in-depth electorate analysis for the Bihar Assembly Election in 2010. The core challenge was to identify the floating/swing voters for each of the parties and to measure their levels electoral apathy, a result of the poor and unchanging condition of the state after 15 years of incumbent rule. In addition to the research phase, CA were tasked to organise the party base at the village level by creating a communication hierarchy to increase supporter motivation. Our client achieved a landslide victory, with over 90% of total seats targeted by CA being won.” In September 2017, reports emerged that the Indian National Congress was in talks with Cambridge Analytica. “The proposal includes building a “national data infrastructure project” for coordinating team planning, strategy and targeted messaging. It also involves identifying the gaps in data that exists in different databases, and making relevant connections using internal and external sources and data analytics to give meaningful insights,” revealed sources at the time. Big data emerged as a key component of elections in India following the 2014 general elections, which saw the BJP and Narendra Modi emerge victorious. Since then, other parties have followed suit, including the Aam Aadmi Party that relied heavily on big data for the foray into Punjab, and the Congress - Samajwadi alliance that made use of big data in the Uttar Pradesh elections. The increasing use of big data also raises questions regarding right to privacy, and the use of fake news to manipulate voters. Reports have shown fake news being spread deliberately by political parties to build narratives that may influence voting behaviour, with big data now making it even easier to target people. Despite these concerns, firms like Cambridge Analytica and the tools of big data analytics remain in hot demand in politics today … misleading information, fake news and manipulation now central to political discourse and behaviour."


line_table=[]
key_table = []
results_table = []
neg_table = []
vsent = vader.SentimentIntensityAnalyzer()

key_country_table = []
key_country_line = []

#fin = open('CASubSet180317StemmedNGram.txt','rt')
#fin = open('CASubSet180320v2.txt','rt')
fin = open('CASubSet180319v2.txt','rt')

for line in fin.readlines():
    print (len(line))
    line_table.append(line)

for l in line_table:    
    if len(l)>7:
        print(l[0:7])
        key_table.append(l[0:6])
        results_table.append(vsent.polarity_scores(l))

for tup in results_table:
    neg1, neu2, pos1, com1  = tup.values()
    neg_table.append(neg1)


    
data = pd.read_csv('CAIndexAll.txt',header=None)
for row, line in data.iterrows():
    key_val = '['+ str(line[0])+']'
    if key_val in key_table:
        ix = key_table.index(key_val)
        key_country_line.append(line[0])
        key_country_line.append(line[1])
        key_country_line.append(line[2])
        key_country_line.append(line[3])
        key_country_line.append(neg_table[ix])
        key_country_table.append(key_country_line)
        key_country_line=[]
        if neg_table[ix]>.02:
            print (line[0]+ ' '+line[2]+ ' ' + line[3])
            print (results_table[ix])

combine_table = []
combine = []
ix = 0
for key in key_table:
    combine.append(key)
    combine.append(neg_table[ix])
    combine_table.append(combine)
    combine = []
    ix+=1
    
print (np.mean(neg_table))

fin.close()
"""
fin = open('CASubSet180320v2.txt','rt')
raw = fin.read()
word_tokens = word_tokenize(raw)
text = nltk.Text(word_tokens)
"""
import csv

with open('results031918v2.csv', 'w', newline='') as out_f: # Python 3
    w = csv.writer(out_f, delimiter=',')        # override for tab delimiter
    w.writerows(key_country_table) 
    
fin.close()

    
"""
use dataframe to sum results by category

"""       
        





"""
raw = fin.read()
fin2 = open('CASubSet180319v2.txt','rt')
raw2 = fin2.read()
fin3 = open('CASubSet180320v2.txt','rt')
raw3 = fin3.read()


word_tokens = word_tokenize(raw)
word_tokens2 = word_tokenize(raw2)
word_tokens3 = word_tokenize(raw3)


text = nltk.Text(word_tokens)
fd = nltk.FreqDist(text)

results = demo_vader_instance(raw)
results = demo_vader_instance(raw2)
results = demo_vader_instance(raw3)


sentim_analyzer = SentimentAnalyzer()
"""
fin.close()