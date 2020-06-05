# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:05:25 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
print(titanic)

print(titanic.groupby('sex')['survived'].mean())
