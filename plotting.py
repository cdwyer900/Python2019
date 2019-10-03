#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:01:47 2018

@author: j2
"""

import pylab
import numpy as N


t = N.arange(0, 10*N.pi,0.1)
y = N.sin(t)

print(N.sin(N.pi))
print (t.dtype)
print(t.size)
print(t)


for i in t:
    print('{}\t {}'.format('%.1f' %i, '%.4f' %N.cos(i)))


pylab.plot(t, y)
pylab.xlabel('t')
pylab.ylabel('y(t)')
pylab.show()