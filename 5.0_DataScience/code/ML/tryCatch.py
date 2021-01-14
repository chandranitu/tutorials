try:
  print(0/0)
except ZeroDivisionError:
  print("cannot divide by zero")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 
