#python3
# demonstrates the python pseudorandom number generator
from random import seed
from random import random

# seed the generator
seed(7)
for _ in range(5):
    print(random())

print(random(),'\n')
# seed the generator to get the same sequence

print('Reseeded--------------------\n')
seed(7)
for _ in range(5):
    print(random())
