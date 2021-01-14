#!/usr/bin/python

class Test(object): 
    # Cosntructor
    def __init__(self,limit):
        self.limit = limit
 
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 9
        return self
 
    # To move to next element. In Python 3,
    #  should replace next with __next__

    def next(self):
        # Store current value ofx        
        x = self.x        
        if x > self.limit:raise StopIteration    # Stop iteration if limit is reached        
        self.x = x + 1;   # Else increment and return old value
        return x

#python2
def next(self): return self.__next__()
 
# Prints numbers from 10 to 15
for i in Test(15) : print(i)
 
# Prints nothing
for i in Test(5) : print(i)
