#python2

import scipy.integrate
from numpy import exp

from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

x, y, z = symbols('x y z')
init_printing(use_unicode=True)


p=symbols('p')
integrate(exp(-p), (p, 0, oo))
