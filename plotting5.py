#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:21:53 2018

@author: j2
"""

import numpy as np
import matplotlib.mlab as mlab # Matlab compatibility commands 
import matplotlib.pyplot as plt

#create matrix Z that contains some interesting data
delta = 0.5
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = mlab.bivariate_normal(X, Y, 3.0, 1.0, 0.0, 0.0)

#display the 'raw' matrix data of Z in one figure
plt.figure(1)
plt.imshow(Z, interpolation='nearest')
plt.title("imshow example 1a: no interpolation")
plt.savefig("pylabimshow1a.pdf")

#display the data interpolated in other figure
plt.figure(2)
im = plt.imshow(Z, interpolation='bilinear')
plt.title("imshow example 1b: with bi-linear interpolation")
plt.savefig("pylabimshow1b.pdf")
