#--------- Lists ----------
# 1- Lists are ordered to use index, and allow duplicate values.
# 2- Lists are mutable, which means you can change the values of the list.
# 3- Lists are written with square brackets.
# 5- Lists can contain any and different data types.
# 6- Lists can be nested.
# 7- Lists can be created with the list() constructor.
# 8- Lists items are not unique.
# 9- Lists uses -1 index to access the last item. 
#---------------------------

list = [1, 2, "my name", ["python", "java", "c++"], 3.14, True]
print(list)
print(list[0]) # the first item from the left = 1
print(list[-1]) # the first item from the right = True = last item

# Slicing
print(list[2:4]) # start from index 2, end at index 4 (not included)
print(list[:4]) # start from index 0, end at index 4 (not included)
print(list[4:]) # start from index 4, end at the last item
print(list[1:-1:2]) # start from index 1, end at index -1 (not included), step 2

# Update item in List
list[0] = "One"

# Accessing the nested list, and Update a slice.
list[3][0:-1] = ["java", "c#"]
print(list)

# Remove range of item from the list
list[2:3] = []
print(list)

list[3:5] = []
print(list)

