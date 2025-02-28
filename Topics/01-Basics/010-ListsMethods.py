#------ List Methods -------
# 1- append() : Add an element to the end of the list.
# 2- len() : Return the number of elements in the list.
# 3- copy() : Return a shallow copy of the list.
# 4- count(x) : Return the number of times x appears in the list.
# 5- extend() : Add all elements of a list to the another list.
# 6- index(x) : Return the index of the first occurrence of x.
# 7- insert(index, object) : Insert the object before the specified index.
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
list = [1, 2, 3, 1, 5]
print(list)
list.append(4)
print(list)
#-------------------------

# 2- len()
print(len(list))
#-------------------------

# very important.
# 3- copy()
# meaning of shallow copy
original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()
print("original: ", original_list)
print("shallow: ", shallow_copy)   

# Modifying the inner list in the original list
original_list[2][0] = 'changed'
print("original: ", original_list)  # Output: [1, 2, ['changed', 4]]
print("shallow: ", shallow_copy)   # Output: [1, 2, ['changed', 4]]
# the change will be reflected in the shallow copy as well,
# because the shallow copy is only a reference to the original list.

original_list.append(5)
print("original: ", original_list)  # Output: [1, 2, ['changed', 4], 5]
print("shallow: ", shallow_copy)   # Output: [1, 2, ['changed', 4]]
# the change will not be reflected in the shallow copy,
# because the shallow copy is a new list that has a reference to the original list.

# Note: if u changed a mutable object in the original list, 
# the change will be reflected in the shallow copy.
# else, the change will not be reflected.

original_list[0] = 'changed'
print("original: ", original_list)  # Output: ['changed', 2, ['changed', 4], 5]
print("shallow: ", shallow_copy)   # Output: [1, 2, ['changed', 4]]
#-------------------------

# 4- count()
print(list.count(1))
#-------------------------

# 5- extend()
a= [1, 2, 3]
b= [4, 5, 6]

a.extend(b)
print(a)

b.extend(a)
print(b)
#-------------------------

# 6- remove()
b.remove(6)
print(b)
#-------------------------

# 7- sort(): ascending order
# note: to sort in descending order: sort(reverse = Ture)
# note: sort() cant use for sorting the list that consists of different elements
b.sort()
print(b)
b.sort(reverse=True)
print(b)
#-------------------------

# 8- reverse()
# important note: the reverse doesn't sort the elems, its just reverse them
a= [3, 5, 7, 8, 9, 6, -1]
a.reverse()
print(a)
#-------------------------

# 9- clear()
a.clear()
print(a)
#-------------------------

# 10- index()
a = ["one", "two", "three", "one"]
print(a.index("one"))
#print(a.index("zero"))
#-------------------------

# 11- insert():
# note -> it doesn't replace the item in the index, its just insert then shift other items
a.insert(0, "zero")
print(a)
a.insert(-1, "zero")
print(a)
#-------------------------

#12- pop()
popped_item = a.pop(0)
print("popped item: ", popped_item)
print(a)
#-------------------------
