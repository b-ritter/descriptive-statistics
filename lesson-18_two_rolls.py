import math
import numpy as np
import matplotlib.pyplot as plt

positions = np.arange(1.5,7, 1)
faces = np.arange(1, 7)

random_cube_two_die_rolls = np.random.randint(1, 7, size=(10000,2))
print(random_cube_two_die_rolls)
means_of_rolls = np.mean(random_cube_two_die_rolls, axis=1)
plt.hist(means_of_rolls, edgecolor='white', bins=np.arange(1, 8, 1))
plt.xticks(positions, faces)
plt.xlabel('Mean of two six-sided dice, 10000 trials')
plt.ylabel('Frequency')
plt.show()