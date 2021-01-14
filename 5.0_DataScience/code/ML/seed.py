# The seed() method is used to initialize the random number generator. The random number generator needs a number to
# start with (a seed value), to be able to generate a random number. By default the random number generator uses the
# current system time.

import random

random.seed(10)
print(random.random())

for i in range(5):
    # Any number can be used in place of '0'.
    random.seed(0)

    # Generated random number will be between 1 to 1000.
    print(random.randint(1, 1000))
