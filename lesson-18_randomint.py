import math
import numpy as np
import matplotlib.pyplot as plt

positions = np.arange(1.5,7, 1)
faces = np.arange(1, 7)
random_cube_die_rolls = np.random.randint(1, 7, size=1000)
print(random_cube_die_rolls)
plt.hist(random_cube_die_rolls, edgecolor='white', bins=np.arange(1, 8, 1))
plt.xticks(positions, faces)
plt.xlabel('Simulation of 1000 random 6-sided dice rolls')
plt.ylabel('Frequency')
plt.show()