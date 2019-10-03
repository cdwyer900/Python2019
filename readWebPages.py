#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:01:49 2018

@author: j2
"""
"""
takes in URLs, reads text, does some preliminary scrubbing
output is big text file
"""

from bs4 import BeautifulSoup, Comment
import requests
import re
import bleach
import numpy.random
import sys

def clean_page(in_page):
    soup1 = BeautifulSoup(in_page.content,'html.parser')
    [x.decompose() for x in soup1.find_all('script')]
    [x.decompose() for x in soup1.find_all('style')]
    [x.decompose() for x in soup1.find_all('meta')]
    [x.decompose() for x in soup1.find_all('noscript')]  
    [x.decompose() for x in soup1.find_all('span')]
    
    for s in soup1(['script','style']):
        s.decompose()
        
    text_parts = soup1.findAll(text=True)

    text = ' '.join(text_parts)


    text2 = re.sub('\n', ' ', text)
    text2 = re.sub('html','',text2)
    text2 = re.sub('  ', ' ', text2)
    text2 = re.sub('  ', ' ', text2)
    p = re.compile(r'data-uri="[\w*\.\/\@-]*\"')

    for match in p.findall(text2):
        text2 = text2.replace(match, '')
        
    p2 = re.compile(r'\[if[ \w\.\=\<\>\:\;\"\/\]\(\)!\|]*?!\[endif\]')
    
    for match2 in p2.findall(text2):
        text2 = text2.replace(match2,'')
        #print(text2)
    return text2

#main
l = []
fin = open('CAIndexv1.csv','rt')
fout = open('CAContentOutAll2.txt','wt') #id number plus text
fout2 = open('CAIndexAll2.txt','wt') #id number plus date & publisher & link
fout.truncate()
fout2.truncate()
num = 0
id_num = 1

for line in fin.readlines():
    num+=1
    #r = numpy.random.randint(0,sys.maxsize)
    #if r % 20 !=0:
    #    continue
    l = line.split(',')
    #url_list.append(l[3])
    #if l[1] == 'SG':
    #    continue

    url = l[3] 
    
    url = re.sub(' ','',url)
    url = re.sub('\n','',url)
    print(url)
    if url.startswith('http'):
        try:
            page = requests.get(url,verify=False,timeout=10)
        except requests.exceptions.RequestException as err:
            print (err)
            continue
    else:
        print(url)
        continue
    if page.ok:
        if re.search('Cambridge Analytica',str(page.content)): 
            # build index line
            s = ('w'+str(id_num))
            line = s+','+line
            out_text = clean_page(page)
            fout.write('['+s+']'+'\n') #write out index value
            fout.write(out_text)
            fout2.write(line)
            print(line)
            print('num read ' +str(num))
            fout.write('\n')
            id_num+=1
        else:
            print(url)
   
  
    #if num >10:
     #   break
 
fin.close()
fout.close()
fout2.close()

    
    
    


