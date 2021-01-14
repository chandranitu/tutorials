class SomeClass(object):
 @classmethod
 def HelloClass(cls, arg):
     pass
## HelloClass = classmethod(HelloClass)
 @staticmethod
 def HelloStatic(arg):
    pass
## HelloStatic = staticmethod(HelloStatic)
#
# Define/implement a decorator.
def wrapper(fn):

 def inner_fn(*args, **kwargs):
     print ('>>')
result = fn(*args, **kwargs)
print ('<<')
return result
return inner_fn
#
# Apply a decorator.
@wrapper
def fn1(msg):
    pass
## fn1 = wrapper(fn1)
