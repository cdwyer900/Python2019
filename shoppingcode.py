#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:11:11 2018

@author: j2
"""

fin = open('shopping_list.txt', 'tr') # INput File 
lines = fin.readlines()
fin.close() # close file as soon as possible

fout = open('shopping_cost.txt', 'tw') # OUTput File 

for line in lines:
    words = line.split()
    itemname = words[0]
    number = int(words[1])
    cost = float(words[2])
    totalcost = number * cost 
    fout.write("{:20} {}\n".format(itemname,totalcost))
    
fout.close()

    
