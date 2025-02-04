#------ List Methods -------
# 1- append() : Add an element to the end of the list.
# 2- len() : Return the number of elements in the list.
# 3- copy() : Return a shallow copy of the list.
# 4- count(x) : Return the number of times x appears in the list.
# 5- extend() : Add all elements of a list to the another list.
# 6- index(x) : Return the index of the first occurrence of x.
# 7- insert() : Insert an item at the defined index.
# 8- pop(index) : Remove the item at the given position in the list, and return it.
# 9- remove(x) : Remove the first item from the list whose value is x.
# 10- reverse() : Reverse the order of the list.
# 11- sort() : Sort the items of the list in place.
# 12- del : Remove an element from the list by index.
# 13- max() : Return the largest number in the list.
# 14- min() : Return the smallest number in the list.
# 15- sum() : Return the sum of all elements in the list.
# 16- clear() : Remove all elements from the list.
# -------------------------

# 1- append()
list = [1, 2, 3]
print(list)
list.append(4)
print(list)
#-------------------------

# 2- len()
print(len(list))
#-------------------------

# 3- copy()
# meaning of shallow copy
original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()

# Modifying the inner list in the original list
original_list[2][0] = 'changed'

print(original_list)  # Output: [1, 2, ['changed', 4]]
print(shallow_copy)   # Output: [1, 2, ['changed', 4]]
#-------------------------

