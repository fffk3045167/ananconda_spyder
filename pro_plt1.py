# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:30:07 2019

@author: Administrator
"""

"""
折线图、曲线图
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)

y1 = np.sin(x)
#y2 = 2 * x ** 3 + 3 * x ** 2 + 2 * x + 5
#y3 = np.sin(2 * x) + 2 * np.cos(1 / x)

plt.figure()
plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
plt.show()
