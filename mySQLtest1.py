#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:28:31 2018

@author: j2
use MySQL connector
"""
import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Cathy_900",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
  
mydb.cmd_init_db("mydatabase")
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

print(mydb)

