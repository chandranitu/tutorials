#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])



integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list)
list_sum = sum(integer_list)
# equals 3
# equals 6


x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

#---------

list = [True, False, 1, 1.1, 1+2j, 'Learn', b'Python']

-------
#nested
nested = [[1,1,1], [2,2,2], [3,3,3]]
for items in nested:
	for item in items:
		print(item, end=' ')

