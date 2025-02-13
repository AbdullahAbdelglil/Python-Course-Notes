# ------ File Handling ------
# 1- open(r "file_path", mode): this is the method that responsiple for:
# creating, editing, reading any files from ur pc.
# open() parameters: 
# file: the full path of the file u want to handl it.
# mode: there are different modes:
#       1- "a": Append: open file for appinding text, create one if not exist
#       2- "r" (default): Read: open file for only reading, return error if not exist 
#       3- "w": Write: open file for writing, create one if not exist
#       4- "x": Create: create file, give error if file is exist
#
# Very important note: file systems in any OS, has two types of pathes;
# 1- Absolute path: form root to the current file: C:\Users\Abdullah.Zaky\** and so on
# 2- Relative path: current path, or files in current working dirictory
#
# Sure: Absolute path is better, because it prevent errors like 'file not found' 
# ----------------------------

file = open("abdullah.txt") # Relative path, find file 'abdullah.txt' in the current working dirictory
file = open(r"C:\Users\Abdullah.Zaky\Desktop\abdullah.txt") # Absolute path: find file 'abdullah.txt' in this specific path.

# Ok, how i can know the current working dirictory (cwd) ?
# there is a module in python called 'os' stands for operatig system u can use it
# ----------------------------

import os

# get the current working dirictory
print("current working dirictory: ", os.getcwd())

# get the absolute path for the current file, __file__ : stands for current file or this file
current_file = os.path.abspath(__file__)
print("Absolute path for current file: ", current_file)

# get the parent dirictory for a file: os.path.dirname(file_abs_path)
print("Parent dirictory for the current file: ", os.path.dirname(current_file))

# Change current working dirictory: os.chdir(file_abs_path)
# remove a file from the system: os.remove(path)