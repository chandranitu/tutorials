import numpy
import matplotlib
from matplotlib import pyplot
%matplotlib inline
x=numpy.linspace(-3,3,11);
y=-x**2;
pyplot.plot(x,y);

pyplot.title("curve of y=-x^2")
pyplot.xlabel("x axis")
pyplot.ylabel("y axis")
pyplot.legend("y=x^2");
print("this curve is parabola");
pyplot.grid()
pyplot.show()
