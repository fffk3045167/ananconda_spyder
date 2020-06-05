# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:19:10 2019

@author: Administrator
"""
#要求输出国际象棋棋盘

import sys

for i in range(8):
    for j in range(8):
        if(i + j) % 2 == 0:
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print('')