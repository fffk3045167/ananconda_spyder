# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:33:47 2019

@author: Administrator
"""

"""
柱状图、
"""

import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure()
month_days = 31
x = [i for i in range(1, month_days)]
y = [random.randrange(20, 41) for i in range(1, month_days)]
plt.bar(x, y, colors = "r", label = "金额")
#开启刻度
plt.minorticks_on()

plt.title("一个月的消费情况")
plt.xlabel("一个月(天)")
plt.ylabel("消费金额(元)")
#显示图例
plt.legend()
# plt.xticks(x)
# plt.yticks([i for i in range(0, 41)])
plt.show()

'''
import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure()
month_days = 5
x = [i + 1 for i in range(1, month_days + 1)]
y = [random.randrange(20, 41) for i in range(1, month_days + 1)]
plt.bar(x, y, label="金额", color=["r", "y", "b", "g", "c"])
# plt.minorticks_on()
plt.title("一周的消费情况")
plt.xlabel("一周(天)")
plt.ylabel("消费金额(元)")
plt.legend()
plt.xticks(x, ["星期{0}".format(i + 1) for i in range(0, month_days + 1)])
plt.grid( linestyle="-.", alpha=0.5)
plt.show()

'''

'''
import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure()
month_days = 5
x = [i for i in range(1, month_days + 1)]
y = [random.randrange(20, 41) for i in range(1, month_days + 1)]
plt.bar(x, y, label="本周", width=0.3, color="r")
plt.bar([i + 0.2 for i in x], [i + random.randrange(1, 10) for i in y], label="上周", width=0.3, color="g")
# plt.minorticks_on()
plt.title("本周和上周的消费情况")
plt.xlabel("同比")
plt.ylabel("消费金额(元)")
plt.legend()
plt.xticks([i + 0.05 for i in x], ["星期{0}".format(i + 1) for i in range(0, month_days + 1)])
plt.grid(linestyle="-.", alpha=0.5)
plt.show()
'''