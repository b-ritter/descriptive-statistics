import statistics as st

from scipy.stats import norm, zscore
import numpy as np
import matplotlib.pyplot as plt

from karma import points

m = st.mean(points)

# Sample standard deviation
std = st.stdev(points)

sorted_points = sorted(points)

z_10 = (10-13)/4.8

z_16 = (16-13)/4.8

# print(z_16) # Z-Table: .7357 of vals

# print(z_10) # Z-Table: .2643 of vals

# >>> .7357 - .2643
# 0.47140000000000004

# Z-Score of 1.6 ---> approx. top 5%

#       1.65 = (x - 13)/4.8
# 1.65 * 4.8 = x - 13
#       7.92 = x - 13
#      20.92 = x

# Actual solution takes the value between two z-scores 
# to get a better approximation of 95%

plt.hist(sorted_points, edgecolor='white', bins=np.arange(min(sorted_points), max(sorted_points), 3.0))
plt.xlabel('Karma Points')
plt.ylabel('Frequency')
plt.show()