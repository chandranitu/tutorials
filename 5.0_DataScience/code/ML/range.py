for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)

-----------------------------

for x in range(10):
# go immediately to the next iteration
if x == 3:continue 
# quit the loop entirely
if x == 5:break
print(x)




for x in range(10):print(x, "is less than 10")
