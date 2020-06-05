# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:30:05 2020

@author: Administrator
"""

"""
上下文管理器
1、基于类的实现
"""

"""
1、with语句先暂存了File类的__exit__方法
2、然后它调用File类的__enter__方法
3、__enter__方法打开文件并返回给with语句
4、打开的文件句柄被传递给read_file参数
5、我们使用.read()来读文件
6、with语句调用之前暂存的__exit__方法
7、__exit__方法关闭了文件
"""
class CustomOpen(object):
    def __init__(self, file_name, method):
        self.file = open(file_name, method)
    def __enter__(self):
        return self.file
    def __exit__(self, type, value, traceback):
        return self.file.close()

with CustomOpen('myfile.txt', 'r') as f:
    read_file = f.read()
print(read_file)