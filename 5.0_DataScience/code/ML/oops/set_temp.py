class Set:
def __init__(self, values=None):
"""This is the constructor.It gets called when create a new Set """
s1 = Set()

# empty set
s2 = Set([1,2,2,3]) # initialize with values"""
self.dict = {}      # each instance of Set has its own dict property

# which is what we'll use to track memberships
if values is not None:
for value in values:
self.add(value)

def __repr__(self):
"""this is the string representation of a Set object if you type it at the Python prompt or pass it to str()"""
return "Set: " + str(self.dict.keys())

# we'll represent membership by being a key in self.dict with value True

def add(self, value):
self.dict[value] = True

# value is in the Set if it's a key in the dictionary

def contains(self, value):
return value in self.dict

def remove(self, value):
del self.dict[value]
