# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:10:18 2020

@author: Administrator
"""

#import numpy as np
import pandas as pd

data = pd.Series(range(10,20,3),
                 index = ['a','b','c','d'])
print(data)

print(data.index)