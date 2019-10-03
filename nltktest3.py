#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:56:23 2018

@author: j2
"""
# import nltk
from nltk.stem import SnowballStemmer
import re
# from nltk.tokenize import sent_tokenize, word_tokenize

# step 3:
# remove accounting words from file
# do word stemming
# open input file
# open output file
# read in file one line at a time
# read each token one ata time from each line
# stem each token
# write out stemmed token
# close input file
# close output file

fin = open('TargetCorpusFiltered.txt', 'rt')
fout = open('TargetCorpusStemmed2.txt', 'wt')
fout2 = open('TargetCorpusNotStemmed.txt', 'wt')


ss = SnowballStemmer("english",ignore_stopwords=True)

acct_stopwords=["type","refer","period","account","detail","balanc","tax","standard",
                "definit","plan","name","the", "benefit", "namespac","income","asset","codif",
                "incom","prefix","oper","xbrli","net","cost","share","na",
                "million","fasb","million","expens","includ",
                "amount","report","leas","other","year","member","valu","rate",
                "loss","monetaryitemtyp","credit","cash",
                "statement","link","use","we","no","stock","sale",
                "date","payment","fair","total","interest","current",
                "debt","durat","end","begin","this","item","relat",
                "compens","note","earn","avail","servic",
                "team","defer","invest","target","tabl",
                "unit","februari","januari","option","defin","receiv",
                "schedul","repres","chang","act","award","shall","sheet","continu",
                "fals","estim","store","one","percent","consolid","corpor",
                "month","per","averag","accumul","debit","within",
                "may","instant","form","due",
                "presentationlink","calculationlink",
                "definitionlink","togglenexts","textblockitemtyp",
                "comment","function","percentitemtyp","pershareitemtyp",
                "text","block","week","stringitemtyp","expect","result","capit",
                "price","grant","effect","inform","record","quarter","term",
                "general","payabl","disclosur","financi","liabil",
                "debtinstrumentredemptionperiodfourmemb","oblig","number",
                "transact","inventori","html","document","wdesk",
                "copyright","pension","agreement","equiti","requir","perform",
                "discontinu","weight","entiti","return","amort","compani","xml",
                "equitysecuritiesmemb","edward","householdessentialsmemb",
                "foodandpetsuppliesmemb","durationitemtyp","filercategoryitemtyp",
                "york","yesnoitemtyp","fairvaluemeasurementsrecurringmemb",
                "yes","abstract","file","estimateoffairvaluefairvaluedisclosurememb",
                "hardlinesmemb","sharesitemtyp","integeritemtyp",
                "interestrateswapmemb","geographicdistributionforeignmemb"
                "gilligan"]
for line in fin.readlines():
    # do stemming on token
    for token in line.split():
        token = re.sub(u'\x99', ' ', token)
        token = re.sub(u'\x91', ' ', token)
        token = re.sub(u'\x94', ' ', token)
        token = re.sub(u'\x97', ' ', token)
        token = re.sub(u'\xa6', ' ', token)
        token = re.sub(u'\x90', ' ', token)
        
        # token = token.encode('utf-8',errors="replace")
        if token.isalpha() and len(token)>1:
           # if token.isupper() and (len(token)==2 or len(token)==3):
            if token == "http" or (token.isupper() and token != "FASB"):
                continue
            else:
                tokenout = ss.stem(token)
                if tokenout not in acct_stopwords:
                    fout.write(tokenout.lower()+' ')
                    fout2.write(token.lower()+' ')
                    # print("token: "+token)
                    # print("Stem: "+tokenout)

fin.close()
fout.close()
fout2.close()
