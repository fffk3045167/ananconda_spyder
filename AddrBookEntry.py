# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:19:36 2020

@author: Administrator
"""

class AddrBookEntry(object):

    def __init__(self, name, phone):     #定义构造器
        self.name = name           #设置name
        self.phone = phone         #设置phone
        print('Created instance for :{}'.format(self.name))

    def updatePhone(self, newphone):       #定义方法
        self.phone = newphone
        print('updated phone for:{}'.format(self.name))

"""创建实例（实例化）
"""
john = AddrBookEntry('John Doe', '408-555-1212')
jane = AddrBookEntry('Jane Doe', '650-555-1212')

"""访问实例属性
"""
print('访问john的name:{}\n访问john的phone:{}\n访问jane的name:{}'
      .format(john.name, john.phone, jane.name))

"""方法调用
"""
john.updatePhone('415-555-1212')
