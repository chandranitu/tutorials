#!/usr/bin/python

# + and * operators 

a = [1, 2, 3, 4]
len(a)

a = [1, 2, 3]
b = [4, 5]
a + b

b * 3
a[0:2]
a[1:4]




#pythagorean triplet
n=25
[(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z]


zip([1, 2, 3], ["a", "b", "c"])
