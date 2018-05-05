
zscore_1 = (50 - 60)/40
# print(zscore_1)

zscore_2 = (80 - 60)/40
# print(zscore_2)

# print(.6915 - .5)

zscore_3 = 1.645

# zscore_3 = (x - 60)/40
cost = 40*zscore_3 + 60
# print(cost*1000)

population = 120500

zscore_4 = (100 - 60)/40

# print(zscore_4)
# .8413

houses_over_100k = population - population * .8413
# print(houses_over_100k)

# m = 80, s = 10
# score between 65 and 90

zscore_90 = (90 - 80) / 10
zscore_65 = (65 - 80) / 10

# print(zscore_90, zscore_65)
percent_90 = .8413 # area below curve to left
percent_65 = .0668

# print(percent_90 - percent_65 )

def zscore(score, s=10, m=80):
  return (score - m) / s

def score(zscore, s, m):
  return s*zscore + m

zscore_80 = zscore(80)
zscore_95 = zscore(95) 

# print(zscore_80, zscore_95) # 0.0 1.5

# .9332 - .5

# print(.9332 - .5)


# m = 120, s = 20

# zscore of .53 = .7019
# zscore of .52 = .6985
# approx zscore .525

# .525 = (x - 120)/ 20

# print(score(.525, 20, 120))

# m = 90, s = 10
# 64th percentile zscore --> .355
# .355 = x - 90 / 10
# print(score(.355, 10, 90))


#Do it with scipy

from scipy.stats import norm

# PS6, ex3
# μ = 60
# σ = 40
ex1 = norm(loc=60, scale=40)

# Sanity Check: CDF gives the probability a random variable would be
# less than or equal to a given value.
# If given the median value, the probability should be .5
mid = ex1.cdf(60)
assert mid == .5

# What proportion of "houses" are less than 50k (in thousands)
print(ex1.cdf(50))
# Correct answer: 0.4012936743170763 👍

