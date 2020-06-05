# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:26:14 2019

@author: Administrator
"""

#dictionary
D = {'a': 1,'b': 2,'c': 3}
print(D.get('d','this is none'))
print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

del D['a']
print(D)

print(D.pop('b'))
print(D)

E = {'aa': 11,'bb': 22,'cc': 33,'dd': 44}
print(sorted(E))
print(sorted(E.keys()))