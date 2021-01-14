#!/usr/bin/python

list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
map(lambda x, y: x + y, list_a, list_b)


#Force list

map_output = map(lambda x: x*2, [19, 12, 33, 54])
print(map_output) 

list_map_output = list(map_output)

print(list_map_output) 
