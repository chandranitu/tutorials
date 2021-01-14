#Ramanujam equation
#x+y**0.5 =11
#x**0.5 -y = -1

#Ans - x=9 y=4

import numpy as np
import scipy.optimize as so

def myEqn(z):
    x = z[0]
    y = z[1]
    F = np.empty((2))
    F[0] = x + pow(y,0.5) - 11
    F[1] = (pow(x,0.5) - y) - 1
    return F

zGuess = np.array([0,0])
z = so.fsolve(myEqn,zGuess)
print(z)
