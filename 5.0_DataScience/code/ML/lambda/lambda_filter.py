#!/usr/bin/python
#python2
a = [1, 2, 3, 4, 5, 6,7,8,9,10]
filter(lambda x : x % 2 == 0, a)

#python3
list(filter(lambda x : x % 2 == 0, a))
