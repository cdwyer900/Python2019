#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:14:50 2018

@author: j2
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# create data
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

#some finetuning of plot
plt.xlabel('Smarts')
plt.ylabel('Probability')
#Can use Latex strings for labels and titles: 
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$') 
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)
#save to file
plt.savefig('pylabhistogram.pdf')