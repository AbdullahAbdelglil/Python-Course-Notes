#------------------------------
# 1- All data in python is object
# 2- Object contains elements
# 3- Each element has its own index
# 4- python uses Zero-Based indexing
# 5- python uses [] to access elements within string, list, or tuple
# 6- python enable accessing parts of strings, lists, and tuples
# 7- python uses negative indexing to start reading from end.
#------------------------------

# Indexing:
message = "hello world"
# Reading from start to end, right to left
print(message[0])
print(message[10])

#print(message[15]) # will raise an error: index out of range

# Reading from end, left to right
print(message[-1]) # first character from end
print(message[-11])
#------------------------------

# Slicing
# Syntax:
# [start:end] -> end not included.
# [:end] -> start = 0
# [start:] -> end = n
# [:] -> start = 0, end = n
# [start:end:steps]

print(message[0:5])
print(message[:5])
print(message[6:])

#default step is (1)
# steps tells to method:
#   1- start form (start_idx),
#   2- get the element in their
#   3- walk n steps, or (skip n-1 chars after current index)
#   4- repeat step (2)


print(message[::2]) # skip one char after current index
print(message[::3]) # skip two chars after current index
print(message[::4]) # skip three chars after current index

