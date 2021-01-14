#A generator is something that can iterate over  but whose values are produced only as needed (lazily).
#One way to create generators is with functions and the yield operator:

def lazy_range(n):
"""a lazy version of range"""
i = 0
while i < n:
 yield i
 i += 1
