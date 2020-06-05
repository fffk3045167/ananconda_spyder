# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:22:09 2019

@author: Administrator
"""

"""
几何分布与几何随机变量
期望:E[X] = 1 / P
方差:V[X] = (1-P)/P^2
"""

import numpy as np
from scipy.stats import geom
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

k = np.arange(1, 11)

fig, ax = plt.subplots(2, 1)
fig.suptitle('geometric distribution PMF')
geom_rv_0 = geom(p = 0.5)
geom_rv_1 = geom(p = 0.25)

ax[0].plot(k, geom_rv_0.pmf(k), 'bo', ms = 8)
ax[0].vlines(k, 0, geom_rv_0.pmf(k), colors = 'b', lw = 5, alpha = 0.5)
ax[0].set_title('p = 0.5')

ax[1].plot(k, geom_rv_1.pmf(k), 'ro', ms = 8)
ax[1].vlines(k, 0, geom_rv_1.pmf(k), colors = 'r', lw = 5, alpha = 0.5)
ax[1].set_title('p = 0.25')

plt.show()