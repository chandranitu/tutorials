import numpy.matlib 
import numpy as np 


print (np.matrix('1 2; 3 4'))

#Conjugate Transpose of Matrix
mat = np.matrix('1 2; 3 4')
print (mat)

# Transpose of Matrix
mat = np.matrix('1 2; 3 4')
mat.T

# filled with random data
print (np.matlib.empty((2,2)))

# filled with zero
print (np.matlib.zeros((2,2)))

# 3 by 3 matrix
print (np.matlib.ones((3,3)))
print (np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))
