#factorial

def t(n):
if n <= 1:
return n
else:
return n * t(n ­ 1)
def test():
numbers = [2, 3, 4, 5]
factorials = [t(n) for n in numbers]
print 'factorials:', factorials
if __name__ == '__main__':
test()



lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
