# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:44:39 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import seaborn as sns

sns.set()

fig, ax = plt.subplots(2, 1)
fig.suptitle('binomial distribution RVS')
binom_rv_0 = binom(n = 10, p = 0.5)
binom_rv_1 = binom(n = 10, p = 0.25)

rvs_0 = binom_rv_0.rvs(size = 100000)
rvs_1 = binom_rv_1.rvs(size = 100000)

ax[0].hist(rvs_0, bins = 11, density = True)
ax[0].set_title('n = 10, p = 0.5')

ax[1].hist(rvs_1, bins = 11, density = True)
ax[1].set_title('n = 10, p = 0.5')

print('rvs_0: {}'.format(rvs_0))
print('rvs_1: {}'.format(rvs_1))

plt.show()