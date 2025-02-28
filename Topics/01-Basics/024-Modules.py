# ------ Modules, and built-in modules ------
# Module is a file contains a set of methods
# You can import them in ur app to use
# You can create ur own module
#
# Syntax 
# 1- to immport the full module: 
# import module_name
# mod.function(): to use the function
# To show all function inside module: use dir(mod_name)

# 2- to immport a specific func form the module:
# form module_name import func_name_1

# You can import more than one mod or func like this:
# import mod1, mod2, mod3, ..
# from mod import func1, func2, func3, ..
# form mod import *: to import all functions
#
# You can add alias to the module or the func, and call it using this alias
# import module_name as name 
# -------------------------------------------

# random module

# 1- 
# import random
# Show all functions in this module
# print(dir(random))


#2- 
from random import randint
print(randint(1, 100))


# ------ Craete ur own module ------
# to create ur own module follow these steps
# 1- create ur file.py and write the methods in it.
# 2- import sys
# 3- append the path of the folder that contains ur module: sys.path.append(r"path")
# 4- import ur module
#
# sys.path: retuns all pathes that python search about modules in it
# ----------------------------------

import sys
# print(sys.path)
sys.path.append(r"C:\Users\EGYPT SOFT\Desktop\Python-Course-Notes\Problem Solving\Course Exercises")

import SliceEmail
print(dir(SliceEmail))

print(SliceEmail.slice("abdullah@gmail.com"))