#flatten nested list
#pip install functools

from functools import reduce
l = [[1,2,3],[4,5,6], [7], [8,9]]
reduce(lambda x,y: x+y,l)

--------------
import operator
l = [[1,2,3],[4,5,6], [7], [8,9]]
reduce(operator.concat, l)

----------------

from collections import Iterable
def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


lst = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
list(flatten(lst)) 
------------

-----------------
def flatten_list(a, result=None):
    """Flattens a nested list."""
if result is None:
 result = []
for x in a:
if isinstance(x, list):
 flatten_list(x, result)
else:
 result.append(x)
return result
