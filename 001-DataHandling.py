# -----------------------------
# type() built-in function in python informs u what is the data type for your object
# All data types in python are variables
# -----------------------------

print(type(10)) # int -> integer
print(type(11.5)) # float -> floating point
print(type("Ten")) # str -> string
print(type(True)) # bool -> boolean
print(type([1,2,3,4])) # list
print(type((1,2,3,4))) # tuple
print(type({"id":1, "name": "EGYPT", "Gender":"male"})) # dict -> dictionary

#------ Key differences between list & tuple in python ------#
# 1- Mutability :
#   List: Lists is mutable, meaning you can change their content after creation (add, remove, or modify elements).
#   Tuple: Tuples is immutable, meaning you can't change their content after creation

# 2- Syntax:
#   List: Lists are defined using square brackets []
#   Tuple: Tuples are defined using parentheses ()

# 3- Performance:
#   List: Lists are generally slower for certain operations because they are mutable and require more memory to handle dynamic changes.
#   Tuple: Tuples are faster and more memory-efficient because they are immutable and have a fixed size.

# 4- Size:
#   List: Lists take up more memory because they are designed to be resized.
#   Tuple: Tuples are more memory-efficient due to their fixed size.
#-------------------------------------------------------------

#Explaining mutability:
my_list = [1,2,3]
my_tuple = (1,2,3)

# will run successfully
my_list[0] = 10

# raises an error: 'tuple' object does not support item assignment
my_tuple[0] = 10
