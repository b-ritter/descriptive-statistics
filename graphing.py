from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# μ = 60
# σ = 40

# Instance of a scaled normal distribution
dist1 = norm(loc=60, scale=40)

x = np.linspace(-140, 260)

plt.plot(x, dist1.pdf(x))
plt.show()

# print(x)