# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:30:05 2020

@author: Administrator
"""

import thinkplot
import matplotlib.pyplot as pyplot


d = {}
for line in open('data.txt'):
    t = line.split()
    size, stride, time = int(t[1]), int(t[3]), float(t[5])
    d.setdefault(stride, []).append((size, time))

thinkplot.PrePlot(num=7)
for stride in sorted(d.keys()):
    if stride >= 512: 
        continue
    
    xs, ys = zip(*d[stride])
    thinkplot.plot(xs, ys, label=str(stride))
    print (stride, len(d[stride]))

pyplot.xscale('log', basex=2)
thinkplot.show(xlabel='size (B)', ylabel='access time (ns)')