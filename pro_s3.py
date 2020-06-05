# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:12:53 2020

@author: Administrator
"""

"""
反转字符串
输入str = 'hello',输出 'olleh'
"""

str1 = input('请输入字符串:')
str2 = []
str3 = []
for x in str1:
    str2.append(x)

while len(str2) - 1 >= 0:
    str3.append(str1[len(str2) - 1])
    str2.pop()
print('反转之后为:', end = '')
for x in str3:
    print(x, end = '')