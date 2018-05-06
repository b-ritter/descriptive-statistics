import math
import statistics as st

import numpy as np
import matplotlib.pyplot as plt

tetrahedral = [1, 1.5, 2, 2.5, 1.5, 2, 2.5, 3, 2, 2.5, 3, 3.5, 2.5, 3, 3.5, 4]

print(st.mean(tetrahedral))

# >>> np.arange(1,5,.5)
# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
plt.hist(tetrahedral, edgecolor='white', bins=np.arange(1, 5, .5))
plt.xlabel('Mean sum of two tetrahedral dice')
plt.ylabel('Frequency')
plt.show()

def pop_std_dv(arr):
  return math.sqrt(st.pvariance(arr))

pop_sigma = pop_std_dv([1,2,3,4])
sample_sigma = pop_std_dv(tetrahedral)

ratio_of_stdv = pop_sigma/sample_sigma # Ratio is square root of sample size!

print(ratio_of_stdv)