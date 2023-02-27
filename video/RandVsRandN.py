# youtube.com/@ailearningcorner ---------
# Numpy rand verses randn
import matplotlib.pyplot as plt
import numpy as np

# Generates random from uniform
# distribution
uniform = np.random.rand(1000)

# Generates uniform from normal
# distribution with mean = 0
normal = np.random.randn(1000)

#Lets Plot
# plt.hist(uniform)
# plt.show()

plt.hist(normal)
plt.show()