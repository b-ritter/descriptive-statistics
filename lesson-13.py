friends = [9, 35, 74, 150, 237, 223, 152, 81, 32, 7]
total_friends = sum(friends)
rel_freq = [friend/total_friends for friend in friends]
print(rel_freq)