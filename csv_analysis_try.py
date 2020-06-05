# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:43:02 2019

@author: Administrator
"""

"""
日期处理

import datetime

strdate = '2019/11/21'
def str_date(sdate):
    return datetime.datetime.strptime(
            sdate, '%Y/%m/%d').date()
#d = datetime.datetime.strptime(strdate, '%Y/%m/%d')
#print(d.date())
#print(d.date().weekday())
print(str_date(strdate))
"""

"""
综合分析
"""
import numpy as np
import datetime

def datestrtonum(bytedate):
    return datetime.datetime.strptime(
            bytedate.decode('utf-8'),'%Y/%m/%d').date().weekday()

dates,c = np.loadtxt('datefile.csv', delimiter = ',', usecols = (0,1), 
                   converters = {0: datestrtonum}, unpack = True)

averages = np.zeros(5)
for i in range(5):
    index = np.where(dates == i)
    prices = np.take(c, index)
    avg = np.mean(prices)
    averages[i] = avg
    print("Day {} prices: {}, avg = {}".format(i, prices, avg))

top = np.max(averages)
top_index = np.argmax(averages)
bot = np.min(averages)
bot_index = np.argmin(averages)
print('highest: {}, top day is {}'.format(top, top_index))
print('lowest: {}, bottom day is {}'.format(bot, bot_index))

"""
裁剪函数
"""
a = np.arange(5)
print(a.clip(1,3))

"""
筛选函数
"""
a = np.arange(5)
print(a.compress(a > 2))