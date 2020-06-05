# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:43:08 2020

@author: Administrator
"""

"""父类
"""
class AddrBookEntry(object):

    def __init__(self, name, phone):     #定义构造器
        self.name = name           #设置name
        self.phone = phone         #设置phone
        print('Created instance for :{}'.format(self.name))

    def updatePhone(self, newphone):       #定义方法
        self.phone = newphone
        print('updated phone for:{}'.format(self.name))


"""子类
"""
class EmplAddrBookEntry(AddrBookEntry):   #继承
    
    def __init__(self, name, phone, empid, email):
        AddrBookEntry.__init__(self, name, phone)
        self.empid = empid
        self.email = email

    def updateEmail(self, newemail):
        self.email = newemail
        print('update e-mail address for:{}'.format(self.name))

"""创建实例（实例化）
"""
john = EmplAddrBookEntry('John Doe', '408-555-1212', 69, 'john@spam.doe')

"""访问实例属性
"""
print('访问john的name:{}\n访问john的phone:{}\n访问john的empid:{}\n访问john的e-mail:{}'
      .format(john.name, john.phone, john.empid, john.email))

"""方法调用
"""
john.updatePhone('415-555-1212')   #调用父类方法
john.updateEmail('john@doe.spam')  