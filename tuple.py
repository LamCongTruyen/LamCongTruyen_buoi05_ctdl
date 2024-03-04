new_tuple = ('a','b','c','d','e')
my_tuple = (1,2,3,4,5)
my_tuple2 = (1,1,1,1,1)
print('a' in new_tuple)#true
print(new_tuple.index('c'))#2
print(my_tuple + my_tuple2)#(1, 2, 3, 4, 5, 1, 1, 1, 1, 1)
print(my_tuple.count(2))


list = [0,1,2,3,4,5,6,7]
list[1] = 3
print(list)#[0, 3, 2, 3, 4, 5, 6, 7]

