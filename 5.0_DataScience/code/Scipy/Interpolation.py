import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
print x,y

plt.plot(x, y)
plt.plot(x, y,'o')
plt.show()

#1D interpolation
