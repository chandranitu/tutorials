import shelve

integers = [11, 21, 3, 4, 51,23]

# Python 2.7, import contextlib and use
# the line:# with contextlib.closing(shelve.open('shelf-example', 'c')) as shelf:
with shelve.open('shelf-ex', 'c') as shelf:
    shelf['ints'] = integers



---------------------

import shelve

with shelve.open('shelf-ex', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key])))
