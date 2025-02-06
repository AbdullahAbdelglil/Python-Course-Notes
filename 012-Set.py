# ----- Set -----
# Set is a collection of unique elements.
# Set is unordered and unindexed.
# Set is represented by curly braces {}.
# Set is mutable.
# Values in set must be immutable, means it cant store list or dictionary.
# Slice and index are not supported in set.
# Set can be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# ----------------

# Set creation
myset1 = {1, 2, 3, 4, 5}
print(myset1) 

myset2 = {1, "one", 2, "two", True, (1, 2, 3)}
print(myset2) # the output is unordered, each time u run the code, the output will be different.
# ----------------

# Set is unordered, why ?
# Set is unordered because it doesn't have index.
# So, u can't access set elements by index.
# The inner working of set is based on hash table.
# Hash table is a data structure that stores key-value pairs.
# Hash table uses a hash function to compute an index into an array of buckets or slots, 
# from which the desired value can be found.
# Since the hash value varies each time u run the code, the output will be different.