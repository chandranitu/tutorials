pure_tuple = ()
print (pure_tuple)

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

---------------

first_tuple = (3, 5, 7, 9)
second_tuple = ('learn', 'python 3')
nested_tuple = (first_tuple, second_tuple)
print(nested_tuple)

-----------------

sample_tuple = ('Python 3',)*3
print(sample_tuple)

----------
sample_tuple = (0 ,1, 2, 3, 4)

tuple_without_first_item = sample_tuple[1:]
print(tuple_without_first_item)

#reverse
tuple_reverse = sample_tuple[::-1]
print(tuple_reverse)

tuple_from_3_to_5 = sample_tuple[2:4]
print(tuple_from_3_to_5)
