import numpy as np
import matplotlib.pyplot as plt
from functools import partial
import matplotlib.pyplot as plt

def difference_quotient(f, x, h):
 return (f(x + h) - f(x)) / h
 
def square(x):
 return x * x
 
def derivative(x):
 return 2 * x

derivative_estimate = partial(difference_quotient, square, h=0.00001)
# plot to show they're basically the same

x = range(-10,10)
plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label='Actual') # red x
plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate') # blue +
plt.legend(loc=9)
plt.show()