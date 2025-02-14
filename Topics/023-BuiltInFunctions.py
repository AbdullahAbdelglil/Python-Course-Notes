# ------ Built-in functions ------
# 01- all(iterable): 
# returns true if all elements in the iterable object is true
#
# 02- any(iterable): 
# returns true if at least one element in the iterable object is true
#
# Note: true elements: anything else: 0, False, empty (list, tuple, string, or dict)
#
# 03- bin(decimal): 
# convert the decimal number to its equivalent binary
#
# 04- id(object): 
# returns a unique integer identifier for an object, 
# which corresponds to its memory address during the object's lifetime.
#
# 05- sum(iterable, start=0): 
# returns the sum of the values in ur iterable.
# note: start is the initial value of the result, so if start is x:
# the result will be list_items + x.

# 06- round(floatnumber, numofdigits): returns the rounded value of this number
# 07- range(start=0, end, step=1): almost used for loop
# 08- print()

# 09- abs(number): returns the distance between ur number and zero, in other words: converts then negative to positive

# 10- pow(): like **
# 11- min(num1, num2)
# 12- max(num1, num2)
# 13- slice()

# 14- map(func, iterable): Transforms each element using the func
# usage: When you need to modify all elements in a sequence
# returns: A new list/iterator of modified values

# 15- filter(func, iterable): Filters elements based on a condition in the func, func must returns boolean
# usage: When you need to remove unwanted elements
# returns: A new list/iterator of selected elements

# 16- reduce(func, iterable): is a function from the functools module that reduces an iterable
# into a single value by applying a function cumulatively, like product, sum, factorial, max-num 
# usage: When you need a single value from a list (product, sum, sub)
# returns: single value u need

# 17- enumerate(iterable, start=0): returns ur iterable object counted. or enumerated
# 18- help(func_name): returns a briefe document of the passed function
# 19- reversed(iterable): reverses the iterable object.
# --------------------------------

# 1- all()
mylist = [1,2,3,4]
print(all(mylist))  # True
print("-"*20)

mylist = [0,1,2,3]
print(all(mylist))  # False, because 0 is False
print("-"*20)

# 2- any()
mylist = [0,"", [], (), {}, 1]
print(any(mylist)) # True, because 1 is True
print("-"*20)

# 3- round()

print(round(5.4))
print(round(5.50))
print(round(5.51))
print(round(5.556, 2))
print("-"*20)

# 5- range()
print(list(range(0))) # empty list, because when u pass 1 arg, it will be used as end.
print(list(range(10))) # [0,1,2,3, ... , 9]

# usage in for loop:
for i in range(0,10):
    print(i)
print("-"*20)

for i in range(0,10,2):
    print(i)
print("-"*20)

# print(message, sep, end): there are alot of info there

# firstly: u can print more than one string using the same print()

print("Abdullah", "From Egypt", "23 Y.O") # Abdullah From Egypt 23 Y.O
print("-"*20)
# note: by default it separates between messages using white space, but u can change it
# adding sep argument

print("Abdullah", "Java Developer", "ITI", sep= " | ")
print("-"*20)

# now the default behaviour in print() is println(), what if i want to make it 
# just print the message, dont add \n ?
print("without using end parameter: ")
print("first line")
print("second line")
print("-"*20)

print("using end parameter: ")
print("first line", end = " ")
print("second line")
print("-"*20)


# 14- map()
def fromat_name(name):
    return f"| {name} |"

names = ["abdullah", "yousuf", "ehab", "tata"]

names = map(fromat_name, names)
names_list = list(names)

for name in names_list:
    print(name)
    
print("-"*20)

# 15- filter()
def even(num):
    return num%2 == 0

my_nums = [1,2,3,4,5,6,8,7,10]
even_nums = filter(even, my_nums)
for num in even_nums:
    print(num)
print("-"*20)

# 16- reduce()
# lets try to calculate the factorial of a number using it:
from functools import reduce

n = 5
nums = list(range(1, n+1))

def product(x, y):
    return x*y

factorial = reduce(product, nums)
print(factorial)
print("-"*20)

# 17- enumerate()

skills = ["Java", "Spring", "Python", "Hibernate", "JPA", "MongoDB"]
enumerated_skills= enumerate(skills, 1)

print("My skills: ", skills)
print("-"*20)

print("My skills enumerated: ", list(enumerated_skills))
print("-"*20)