#!/usr/bin/python

#list
print("List Iteration")
lst = ["ram", "for", "shyam"]
for i in lst: print(i)

#tuple
print("\nTuple Iteration")
t = ("ram1", "for", "shyam1")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "chandra"
for i in s : print(i)
     
# Iterating over dictionary

print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
d['a']=135
d['b']=456

for i in d : print("%s  %d" %(i, d[i]))

