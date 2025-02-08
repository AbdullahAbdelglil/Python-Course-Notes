# ------- Data Type Conversion -------
# 1- str(object): converts anything to string
# 2- tuple(iterable object): converts any iterable object to tuple
# 3- list(iterable object): converts any iterable object to list, like tuple
# 4- set(iterable object): converts any iterable object to set.
# 5- dict(): converts list, nd tuple to dict, but note: there is limitations
# important notes:
    # 1- when u convert from set to list or tuple: the order of items will change.
    # 2- when u convert from dict to list, set or tuple: only the keys will be considered.
    # 3- when u convert from any iterable object to set:
        # -> the repeated items will be deleted
        # the order of items will be changed.
    # 4- converting from tuple and list to dict notes:
        # 1- tuple, list must consist key and value, u can apply this by nested.
        # 2- u cant convert from set to dict, because the set isn't hashable
# ------------------------------------

# 1- str()
a = 10
b = 15.5
print(type(a))
print(type(b))
a = str(a)
b = str(b)
print(type(a))
print(type(b))
print("-"*50)
# ------------------------------------

#2- tuple()
a = "ahmed"
b = [1,2,3]
c = {4,5,6}
d = {"one":1, "two":2, "three":3}
e = 100

print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = tuple(a)
b = tuple(b)
c = tuple(c)
d = tuple(d) # will extract the keys only

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# e = tuple(e) # raises an error
print("-"*50)
# ------------------------------------

# 3- list() like tuple()
# ------------------------------------

# 4- set()
a = "ahmed amjad"
b = [1,2,3,1,3]
c = {4,5,6,6,5}
d = {"one":1, "two":2, "three":3}

print(set(a))
print(set(b))
print(set(c))
print(set(d))
print("-"*50)
# ------------------------------------

# 4- dict(): this is the only way that enables u to convert from list, or tuple to dict

b = [["one", 1], ["two", 2], ["three", 3]]
c = (("one", 1), ("two", 2), ("three", 3))

print(dict(b))
print(dict(c))
