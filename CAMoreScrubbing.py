#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 18:29:48 2018

@author: j2
"""

def strip_ifs(line, in_x, in_z):
    out_l=line.replace(z, '')
    return out_l
    


fin = open('CASubSet180322.txt','rt')
fout = open('CASubSet180322v2.txt','wt')
fout.truncate()

pages = []
x = 0
i = 0
for line in fin.readlines(): 
    #print (line)
    x=0
    while (x!=-1):
        x=line.find('[if',i)
        print (x)
        if x!=-1:
            i=x+1
            y=line.find(']',i)
            print (y)
            if y!=-1:
                z = line[x:y+1]
                print (z)
                line = strip_ifs(line, x, z)
                i=0
                #print (line)
    if line !="":
        fout.write(line)    

fin.close()
fout.close()

