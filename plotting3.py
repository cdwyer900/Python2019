#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:41:22 2018

@author: j2
"""

import pylab
import numpy as N

t = N.arange(0, 2 * N.pi, 0.01)

pylab.subplot(2, 1, 1)
pylab.plot(t, N.sin(t))
pylab.xlabel('t')
pylab.ylabel('sin(t)')

pylab.subplot(2, 1, 2)
pylab.plot(t, N.cos(t))
pylab.xlabel('t')
pylab.ylabel('cos(t)')
