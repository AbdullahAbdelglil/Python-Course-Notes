# ----- Set Methods -----
# 1- add() method adds an element to the set.
# 2- clear() method removes all elements from the set.
# 3- copy() method returns a copy of the set.
# 4- difference() method returns a set that contains the difference between two sets.
# 5- union() method returns a set that contains all items from the original set,
# and all items from the specified sets.
# 6- intersection() method returns a set that contains the similarity between two or more sets.
# 7- isdisjoint() method returns whether two sets have a intersection or not.
# 8- issubset() method returns whether another set contains this set or not.
# 9- issuperset() method returns whether this set contains another set or not.
# 10- pop() method removes a random element from the set.
# 11- remove() method removes the specified element from the set.
# 12- discard() method removes the specified element from the set.
# differnce between remove() and discard() is that:
# if the element is not found, remove() will raise an error, but discard() will not.
# 13- update() method updates the set with the union of this set or list or others.
# 14- symmetric_difference()method returns a set containing elements that are in either of the sets, but not in both.
# -----------------------


# 1- add()
myset1 = {1, 2, 3, 4, 5}
myset1.add(6)
print(myset1) 
# -----------------------

# 2- clear()
myset1.clear()
print(myset1) 
# -----------------------

# 3- union()  
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {7, 8, 9}

# trick for union
print(set1 | set2 | set3)

# union using union() method
set4 = set1.union(set2, set3) 
print(set4)
# -----------------------

# 4- update()
set1.update(set2, set3)
print(set1)

list = [0, -1, -5]
set1.update(list)
print(set1)
# -----------------------

# 5- difference():
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1)
print(set1.difference(set2))
print(set1)

# also u can apply difference using (-) operator
print(set1 - set2)

# difference_update(): removes the items that exist in both sets.
a = {1,2,3,4}
b = {3,4,5,6}
a.difference_update(b)
print(a)
# -----------------------

# 6- intersection():
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1)
print(set1.intersection(set2))
print(set1)

# also u can apply difference using (&) operator
print(set1 & set2)

# intersection_update(): removes the items that is not present in both sets.
a = {1,2,3,4}
b = {3,4,5,6}
a.intersection_update(b)
print(a)
# -----------------------

# 7- symmetric_difference():
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 5, 6}

# also u can apply difference using (^) operator
print(set1 ^ set2)

# symmetric_difference_update(): removes the items that is not present in both sets.
a = {1,2,3,4}
b = {3,4,5,6}
a.symmetric_difference_update(b)
print(a)
# -----------------------

# 8- issuperset(), 9- issubset():
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = {1, 2, 3, 6}

print(set1.issuperset(set2))  # Output: True
print(set1.issuperset(set3))  # Output: False

print(set2.issubset(set1)) # Output: True
print(set3.issubset(set1)) # Output: False
# -----------------------

# 10- isdisjoint():
set1 = {1, 2, 3, 4, 5}  
set2 = {6, 7, 8, 9, 10}
set3 = {5, 6, 7, 8, 9}

print(set1.isdisjoint(set2))  # Output: True
print(set1.isdisjoint(set3))  # Output: False
# -----------------------