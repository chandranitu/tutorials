import sys
sys.float_info

----------

num = 2
print("The number (", num, ") is of type", type(num))

num = 3.0
print("The number (", num, ") is of type", type(num))

num = 3+5j
print("The number ", num, " is of type", type(num))
print("The number ", num, " is complex number?", isinstance(3+5j, complex))


------------
num = 1234567890123456789
num.bit_length()

