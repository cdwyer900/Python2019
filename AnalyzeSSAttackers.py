#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:12:29 2019

@author: catherineadwyer
"""

import pycountry
import string
import operator

fin=open('StateCountriesAttackers.txt', 'rt')
str1 = fin.read()
str1 = str1.replace(',', ' ')
ssList = []
ssCountList = []

"""
find all tokens that begin with SS- and add them to list
"""
for word in str1.split():
    if word.startswith("SS-") and word not in ssList:     
        ssList.append(word)
        value = str1.count(word)
        item = (word,value)
        ssCountList.append(item)
"""
need to fix problem with two word country names like North Korea
"""


fin.close()
