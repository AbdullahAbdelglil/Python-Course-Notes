# ------ Built-in functions ------
# 1- all(iterable): 
# returns true if all elemnts in the iterable object is true
#
# 2- any(iterable): 
# returns true if at leats one elemnts in the iterable object is true
#
# Note: true elements: any thing else: 0, False, empty (list, tuple, string, or dict)
#
# 3- bin(decimal): 
# convert the decimal number to its equivalent binary
#
# 4- id(object): 
# returns a unique integer identifier for an object, 
# which corresponds to its memory address during the object's lifetime.
#
# 5- sum(iterable, start=0): 
# returns the sum of the values in ur iterable.
# note: start is the initial value of the result, so if start is x:
# the result will be list_items + x.

# 6- round(floatnumber, numofdigits): retuns the rounded value of this number
# 7- range(start=0, end, step=1): almost used for loop
# 8- print()
#
# --------------------------------

# 1- all()
mylist = [1,2,3,4]
print(all(mylist))  # True
print("-"*20)

mylist = [0,1,2,3]
print(all(mylist))  # Flase, , because 0 is False
print("-"*20)

# 2- any()
mylist = [0,"", [], (), {}, 1]
print(any(mylist)) # True, because 1 is True
print("-"*20)

# 3- roubd()

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
# note: by default it separtes between messages using white space, but u can change it
# adding sep argument

print("Abdullah", "Java Developr", "ITI", sep= " | ")
print("-"*20)

# now the default behaviour in print() is println(), what if i want to make it 
# just print the message, dont add \n ?
print("without usign end parameter: ")
print("first line")
print("second line")
print("-"*20)

print("usign end parameter: ")
print("first line", end = " ")
print("second line")
print("-"*20)
