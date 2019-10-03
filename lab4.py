#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:15:21 2018

@author: j2
"""

# reads in a file containing numbers separated by spaces
# computers and prints the sum for each line

def print_line_sum_of_file(inFile):
    fin = open(inFile, 'tr')
    lines = fin.readlines()
    fin.close()
    
    #computes and prints the sum for each line
    sum=0
    counter = 1
    i=0
    for line in lines:
        print("line "+ str(counter)+":",line)
        x = line.split(' ')
        for i in x:
            #print(i)
            sum += int(i)
            
        print("line", counter,"total = ", sum)
        counter+=1
        sum = 0
        print("")
            
    print("outer loop ends")
    
print_line_sum_of_file("inNums.txt")
        
            
            