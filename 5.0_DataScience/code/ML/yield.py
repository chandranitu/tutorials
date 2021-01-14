#iterable
list1 = [1, 2, 3,4,5]
for i in list1:
 print(i)

#list1 is iterable
#useing a list comprehension, create a list

list2 = [x*x for x in range(5)]
for i in list2:
 print(i)


#Generators
#Generators are iterators, a kind of iterable can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
#It is just the same except you used () instead of []. BUT, cannot perform for i in mygen a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 25, one by one.

mygen = (x*x for x in range(6))
for i in mygen:
 print(i)

#yield
#yield is a keyword that is used like return, except the function will return a generator.

def createGen():
 mylist = range(5)
 for i in mylist:
  yield i*i

mygenerator = createGen()
 print(mygenerator)



