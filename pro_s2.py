# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:10:30 2019

@author: Administrator
"""

"""
字符串匹配

"""

import re

line = 'this is a test procedure'
numbers = '1251 55 135 11'
pattern = r'a t'
print(re.sub(r' ','',numbers))
m = re.search(pattern, line)
print(m)