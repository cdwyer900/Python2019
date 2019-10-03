#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 16:00:29 2018

@author: j2
"""

import nltk
from nltk.tokenize import word_tokenize

fin1 = open('combined_text.txt','rt')
raw = fin1.read()

raw = raw.replace('social media','social_media')
raw = raw.replace('social network','social_network')
raw = raw.replace('user data', 'user_data')
raw = raw.replace('personal information','personal_information')
raw = raw.replace('third parties','third_party')
raw = raw.replace('third party','third_party')
raw = raw.replace('personality traits','personality_traits')
raw = raw.replace('psychological profiles','psychological_profiles')
 


word_tokens = word_tokenize(raw)
text = nltk.Text(word_tokens)




