# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:06:21 2019

@author: Administrator
"""

#文本文件读取时的编码解码
str1 = '这是一个例子！'

with open('utf-8file.txt', 'w', encoding = 'utf-8') as f:
    f.write(str1)

with open('utf-8file.txt', 'r', encoding = 'utf-8') as f:
    f_str1 = f.read()

print(f_str1)

"""
因为文本字符串在存储到磁盘的时候会编码成字节字符，
所以可以先以字节字符串的形式从文件中将其读取，然后再进行解码。
"""

with open('utf-8file.txt', 'rb') as f:
    f_byte1 = f.read()

print(f_byte1)
print(f_byte1.decode(encoding = 'utf-8'))

#文件操作
"""
利用内置函数open进行文件操作时，第一个参数是文件名，第二个参数是处理模式。
典型的使用模式参数有：r为以只读模式打开文件，w为输出模式打开文件，a代表在文件尾部追加内容而打开文件，
模式字符串尾部加上b可以进行二进制数据处理。内置open函数会创建一个python文件对象，作为文件操作的接口。
"""

my_str1 = open('myfile.txt', 'w')
my_str1.write('strat file\n')
my_str1.write('file end\n')
my_str1.close()
"""
readline方法：一次读取一行
"""
my_str1 = open('myfile.txt', 'r')
print(my_str1.readline())
print(my_str1.readline())
"""
read方法：一次读取全部内容
"""
my_str2 = open('myfile.txt', 'r')
print(my_str2.read())
"""
文件迭代器，逐行扫描
"""
my_str3 = open('myfile.txt', 'r')
for line in my_str3:
    print(line, end = '')

"""
二进制文件读写
"""
my_byte1 = open('eee.bin', 'wb')
my_byte1.write(b'qwer')
my_byte1.close()

b_file = open('eee.bin', 'rb')
b_data = b_file.read()
b_file.close()
print(b_data)
print(list(b_data))

"""
pickle模块是能够让我们直接在文件中存储几乎任何Python对象的高级工具
"""
import pickle
D = {'a': 1, 'b': 2, 'c': 3}
L = [3, 4, 5]
with open('datafile.pkl', 'wb') as file:
    pickle.dump(D, file)
    pickle.dump(L, file)

with open('datafile.pkl', 'rb') as file:
    print(pickle.load(file))
    print(pickle.load(file))
file.close()