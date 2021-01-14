import random
four_uniform_randoms = [random.random() for _ in range(4)]


random.seed(10)
print (random.random())
random.seed(10)
print (random.random())




----------------

from random import shuffle
x = ['Keep', 'The', 'Green', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
