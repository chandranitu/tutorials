#python2
#pip install sympy

from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

diff(cos(x), x)

diff(cos(x), x,x)

diff(exp(x**2), x)

diff(x**4, x, x, x)
