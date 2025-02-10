# ----- Tuples -----
# Tuple are similar to list, but it is immutable, 
# meaning that the values inside a tuple cannot be changed.
# Tuple items are enclosed in parentheses.
# U can remove parentheses if u want, but it's not recommended.
# 
# ------------------

# Tuble immutabllity
tuple1 = (1, "tow", 3, 4, [5, 6, 7])
print(tuple1)

# tuple1[2] = "three" # This will raise an error
# TypeError: 'tuple' object does not support item assignments
# ------------------

# Tuple with single item
tuple2 = ("one")
print(type(tuple2)) # <class 'str'>

tuple2 = ("one",)
print(type(tuple2)) # <class 'tuple'>
# ------------------

# Tuple unpacking
tuple3 = (1, 2, 3)
a, b, c = tuple3
print(a, b, c)
# ------------------

# Tuple concatenation
tuple4 = (1, 2, 3)
tuple5 = (4, 5, 6)
tuple6 = tuple4 + tuple5
print(tuple6)
# ------------------

# Tuple repetition. 
# note: repetition is not the same as concatenation
# note: repetition can used with list and string as well
tuple7 = (1, 2, 3)
tuple8 = tuple7 * 3
print(tuple8)
# ------------------

# Tuple Methods

# 1- count() method returns the number of times a specified value appears in the tuple.
tuple9 = (1, 2, 3, 4, 1, 1)
print(tuple9.count(1))

# 2- index() method searches the tuple for a specified value and returns the position of where it was found.
print(tuple9.index(3))
# ------------------

# Tuple membership
print(1 in tuple9) # True
print(5 in tuple9) # False
# ------------------

# Tuple destructuring
tuple10 = (1, 2, 3, 4)
a, b, *c = tuple10
print(a, b, c) # 1 2 [3, 4]

a, b, c,_ = tuple10 # use _ to ignore any value
print(a, b, c) # 1 2 [3, 4]
# ------------------
