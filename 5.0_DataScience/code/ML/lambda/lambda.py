#!/usr/bin/python

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
----------

def multiply2(x):
  return x * 2
    
map(multiply2, [2, 2, 3, 4])

OR

map(lambda x : x*2, [2, 2, 3, 4])

---------------


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8},{'name': 'math', 'points': 9}]
  
map(lambda x : x['name'], dict_a) 
  
map(lambda x : x['points']*10,  dict_a) 

map(lambda x : x['name'] == "python", dict_a) 

---------------


 
