# ------ Iterable Vs iterator ------
# Iterable: is an object contains data that can be iterable up on. like (list, str, tuple, ..)
# Iterator: is the object used for iterarting over iterable object using next() method
# u can generate an iteratror for an iterable object using iter(iterable) 
# ----------------------------------

myList=[1,2,4,5,9,8,7]
list_iterator = iter(myList)

for i in (list_iterator):
    print(i, end=" ")
