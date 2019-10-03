#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:53:49 2018

@author: j2

change DoD pdf to txt
change to pypdf2

"""
import PyPDF2
from bs4 import BeautifulSoup
import nltk
import re

pdf_file = open('DOD2015.pdf','rb')
fout = open('DOD2015.txt','wt')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
soup = BeautifulSoup("<a><b /></a>", "lxml")
# regex of printable characters

num_pages = read_pdf.getNumPages()
pages=[]

raw_text = ""
tt = ""
text=""


for i in range(0,num_pages):
    page = read_pdf.getPage(i)
    pages.append(page)
    
for i in range(len(pages)):
    # print(pages[i].extractText())
    t = pages[i].extractText()
    soup = BeautifulSoup(t)
    text_parts = soup.findAll(text=True)
    text = ' '.join(text_parts)
    for j in range(len(text)):
        if text[j].isprintable():
            tt = tt+text[j]
    
    raw_text = raw_text + tt + ' '

fout.write(raw_text)

fout.close()
pdf_file.close()

     




