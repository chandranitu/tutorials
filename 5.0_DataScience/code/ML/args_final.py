# Python program  
# *args 

def testify(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

## with *args
args = ("hello", 42, "chandra")
testify(*args)

# with *kwargs
kwargs = {"arg1" : "hello", "arg2" : 42, "arg3" : "chandra"}
testify(**kwargs)


