frozenset()
cities = {'delhi', 'kolkata', 'patna'}
type(cities)


------------
sample_set = {"red", "green"}
sample_set.add("black")
print("Standard Set")
 print(sample_set)

 # A frozen set
frozen_set = frozenset(["red", "green", "black"]) 
print("Frozen Set")
print(frozen_set)

frozen_set.add("yellow")   # error
