# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:45:54 2019

@author: Administrator
"""

"""
计算两个日期相差的天数
"""

import time
import datetime

def Caltime(date1,date2):
    date1 = time.strptime(date1, '%Y-%m-%d')
    date2 = time.strptime(date2, '%Y-%m-%d')
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return date2 - date1

def is_date(str):
    try:
        time.strptime(str, '%Y-%m-%d')
        return True
    except:
        return False

if __name__ == '__main__':
    print('请输入较早日期(格式例：xxxx-xx-xx)：', end = '')
    while True:
        date1 = input()
        if is_date(date1) == True:
            break
        else:
            print('日期或格式错误，请重新输入正确的日期！')
    print('请输入较晚日期(格式例：xxxx-xx-xx)：', end = '')
    while True:
        date2 = input()
        if is_date(date2) == True:
            break
        else:
            print('日期或格式错误，请重新输入正确的日期！')
    print(Caltime(date1,date2))