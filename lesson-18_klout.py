import math
import random

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from klout import klout

m = np.mean(klout)
s = np.std(klout)
SE = s/math.sqrt(35)
print(SE)

klout_sorted=sorted(klout)

# plt.hist(klout, edgecolor='white', bins=15)
# plt.xlabel('Klout scores')
# plt.ylabel('Frequency')
# plt.show()

# x_axis = np.arange(0,100)
# plt.plot(x_axis, norm.pdf(x_axis, m,SE))
# plt.xlabel('Klout scores')
# plt.ylabel('Frequency')
# plt.show()


ex1 = norm(loc=37.72, scale=2.71)

# Sanity Check: CDF (cumulative distribution function) 
# gives the probability a random variable would be
# less than or equal to a given value.
# If given the median value, the probability should be .5
prob1 = 1 - ex1.cdf(40)

print(prob1) 
# 0.20008198863158877👍

ex2 = norm(loc=37.72, scale=1.0145)

prob2 = 1 - ex2.cdf(40)
print(prob2)
# print((40 - 37.72)/1.01)

avg_5 = np.mean([random.choice(klout) for r in range(0,5)]) 
print(avg_5)

avg_10 = np.mean([random.choice(klout) for r in range(0,10)]) 
print(avg_10)
# 39.01289282
# 22.13182541
# 25.36272899
# 49.96429777
# 24.66350014