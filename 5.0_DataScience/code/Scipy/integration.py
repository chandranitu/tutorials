#python3

import scipy.integrate
from numpy import exp

f= lambda x:x     #f(x)dx
#f= lambda x:exp(-x**2)
i = scipy.integrate.quad(f, 0, 1)
print (i)
#The quad function returns the two values,first number is value of integral and second is estimate of the absolute error in the value of integral.


#Double quad

import scipy.integrate
from numpy import exp
from math import sqrt
f = lambda x, y : 16*x*y
g = lambda x : 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print (i)
