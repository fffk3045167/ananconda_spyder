# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:05:07 2019

@author: Administrator
"""

"""
字符串的赋值
"""
"""
    1、深拷贝
    位于不同内存空间
"""
str1 = ['qwer']
str2 = 'qwer'
str3 = str1[:]
print(str3)
print(str3 is str1)
print(str1 is str2)
print(str1 == str2)
print(type(str1))
print(type(str2))
"""
    2、浅拷贝
    位于同一内存空间
"""
str4 = str2
print(str4)
print(str4 is str2)

"""
字符串的遍历与成员测试
"""

for x in str2:
    print(x, end = ' ')

print('a' in str2)
print('q' in str2)

"""
字符串的查找与替换
"""
"""
查找:find
"""
s1 = 'abcdefg'

print(s1.find('ef'))
print(s1.find('db'))
"""
替换:replace
"""
s2 = 'abcdefg'
print(s2.replace('defg','abc'))

"""
提取与连接
"""
"""
提取:split方法:利用字符串中存在的分隔符，将其拆分成子字符串，并返回其所组成的列表
"""
s3 = 'Tom 21 USA UCLA'
list1 = s3.split(' ')
print(list1)
"""
连接:join方法：使用指定的分隔符将列表中的元素连接成一个字符串，并用指定的分隔符对其进行分割。
"""
list2 = ['s','p','y','d','e','r']
s4 = ''.join(list2)
print(s4)
"""
去空字符方法:strip:去除字符串两侧的空格、回车换行等
"""
s5 = '   Tom 21 USA UCLA\n\n\n'
print(s5)
print(s5.strip())

"""
字符串的格式化输出
"""
name = 'fengke'
age = 22
school = ['HAUT']

s = 'name: {}, age: {}, and graduates from: {}'
s = s.format(name, age, school)
print(s)
"""
特殊的数字输出:浮点指定输出位、二进制输出
"""
str5 = 'float number = {: .2f}'

s6 = str5.format(10.2545825)
print(s6)

str6 = 'number = {: b}'

s7 = str6.format(483)
print(s7)
"""
字符串转义：斜杠：\t  \n等等
字符串前加一个r就能关闭转义机制
"""
str7 = 'c:\new\test.py'
str8 = r'c:\new\test.py'
print(str7)
print(str8)
"""
字符编码

"""
a = '123'
b = b'456'
print(a)
print(type(a))
print(b)
print(type(b))
print(list(b))
"""
编码：encode方法，使用特定编码将该字符串转换为一个bytes
解码：decode方法，接受一个编码作为单个必要参数，并返回一个str
"""
"""
import sys
查看平台
print(sys.platform)
查看平台默认编码
print(sys.getdefaultencoding())
"""
str9 = '七里香πR^2'
bytes1 = str9.encode('utf-8')
print(bytes1)

byte2 = b'\xe4\xb8\x83\xe9\x87\x8c\xe9\xa6\x99\xcf\x80'
str10 = byte2.decode(encoding = 'utf-8')
print(str10)