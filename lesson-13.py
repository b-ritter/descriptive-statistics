import statistics as st


friends = [9, 35, 74, 150, 237, 223, 152, 81, 32, 7]
total_friends = sum(friends)
rel_freq = [friend/total_friends for friend in friends]
print(rel_freq)

scores = [x for x in range(0, 100, 10)]

stdv = st.stdev(scores)
mean = st.mean(scores)

z = lambda i, m, s: (i - m)/s

zscores = [z(score, mean, stdv) for score in scores]

print(zscores)

print(st.mean(zscores))

print([z(s, 20, 3) for s in [20, 17, 21.5]])

print([z(s, 120, 40) for s in [205, 137, 20, 90]])

print(f"Sharon: {z(99, 90, 10)}")

print(f"Steve: {z(95, 90, 10)}")

print(f"Roman: {z(110, 90, 10)}")

# 1.2 = (x - 90) / 10 
print(f"Jill: {1.2 * 10 + 90}")

# 3.0 = 46 - 40 / x
# 3.0 = 6/x
#   x = 6/3.0
#   x = 2