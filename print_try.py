# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:25:51 2019

@author: Administrator
"""

import sys

def print30(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs:
        raise TypeError('extra keywords:{}'.format(kargs))
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
        file.write(output + end)

print30('hello','world','healthy',sep = '&')