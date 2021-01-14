import numpy as np

ar1 = np.array([1,2,3,4,5,6,7,8,9,10]) 
print (ar1)

# more than one dimensions
ar1 = np.array([[1, 2], [3, 4],[13, 14],[23, 24]]) 
print (ar1)

# minimum dimensions 
a = np.array([1, 2, 3,4,5], ndmin = 2) 
print (a)

# minimum dimensions 
a = np.array([1, 2, 3], dtype = complex) 
print (a)
