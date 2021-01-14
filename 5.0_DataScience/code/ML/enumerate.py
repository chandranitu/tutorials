# Python program to illustrate enumerate function

l1 = ["eat","walk","doing","abc"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,2)))

print (list(enumerate(l1,5)))



---------------
#Using Enumerate object in loops

# Python program to illustrate enumerate function in loops
l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
print
# changing index and printing separately
for count,ele in enumerate(l1,100):
    print (count,ele)
