

# importing pandas as pd 

# reshape example
import numpy as np
a = np.zeros((10, 2))

 # A transpose makes the array non-contiguous
b = a.T
c = b.view()

a1 = np.arange(6).reshape((3, 2))
c1=np.reshape(a1, (2, 3)) # C-like index ordering
c1


a = np.array([[1,2,3], [4,5,6]])
np.reshape(a, 6)
  


