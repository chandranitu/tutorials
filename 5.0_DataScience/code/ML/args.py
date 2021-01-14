# Python program  
# *args 

def testify(arg, *argv):
 print ("first argument :", arg)
 for arg in argv:
  print ("Next argument through *argv :",arg)



testify('Hello', 'This', 'is')

testify('Hello', 'This', 'is', 'python','training')
