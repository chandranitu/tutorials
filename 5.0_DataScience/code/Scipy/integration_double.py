#python2

import scipy.integrate
from numpy import exp
from __future__ import division
from sympy import *


x,y=symbols('x y')
integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))

#If integrate is unable to compute an integral, it returns an unevaluated Integral object.

expr = integrate(x**x, x)
print(expr)
expr




expr1 = Integral(log(x)**2, x)
expr1


integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x - exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
