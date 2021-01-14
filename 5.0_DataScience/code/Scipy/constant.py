#Import pi constant from both the packages

from scipy.constants import pi
from math import pi
import numpy as np

#math.pi == np.pi == scipy.pi

print("sciPy - pi = %.16f"%pi)
print("sciPy - pi = %.16f"%scipy.constants.pi)
print("math - pi = %.16f"%math.pi)


res = scipy.constants.physical_constants["alpha particle mass"]
print res
