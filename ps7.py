import math

from scipy.stats import norm

SE = 10
sample_size = 4

# SE   = s/sqrt(n)
# 10   = s/sqrt(4)
# 2*10 = s = 20
# SE_1 = 20/sqrt(16)
# SE_1 = 20/4 = 5 👍

# Ex. 7
s = 20
sample_sizes = [25, 100, 100, 25]
means = [104, 104, 102, 102]

scores = []
for sample, mean in zip(sample_sizes, means):
  SE = 20/math.sqrt(sample)
  zs = (mean - 100)/SE
  scores.append(zs)

print(abs(min(scores)))
# .5 👍


# q11
# μ = 100
# σ = 20
# N = 4
# SE = 10
q11 = norm(loc=100, scale=10)

print(1 - q11.cdf(110))
# .158

# q14
# μ = 100
# σ = 20
# N = 25
# SE = 4
q14 = norm(loc=100, scale=4)
print(1 - q14.cdf(110))

# q22
# SE1 = s/math.sqrt(25)
# SE2 = (1/3) * SE1 = s/math.sqrt(x) 
# SE2 = (1/3) * s/5 = s/math.sqrt(x)
#              1/15 = 1/math.sqrt(x)
#                15 = math.sqrt(x)
#        pow(15, 2) = x
print(pow(15,2))
# 225 👍