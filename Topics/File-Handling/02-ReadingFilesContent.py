
# ------- Reading file --------
# 1- read(num_of_chars = -1): this is the method that reads the file content
#  it accepts the number of chars u need to read, by default = -1, means all chars
# 
# 2- readline(num_of_chars = -1): read one line from the file, by default the first line
# if u repeat this method, it will start from the next line
#
# 3- close(): close the file after each operation (Best Paractice)
# -----------------------------
path = r"C:\Users\Abdullah.Zaky\Desktop\Python-Course-Notes\Topics\File-Handling\abdullah.txt"
file = open(path)

print("file metadata: ", file) # object contains the file metadata
print("file name: ", file.name) # print the file name
print("file mode: ", file.mode) # print the mode; r, w, a, or x
print("file encoding: ", file.encoding) 
file.close()
print("-"*50)

# to print the file content
file = open(path)
print("file content:\n", file.read())
file.close()
print("-"*50)

# to print the file content line by line
file = open(path)
print("file content line by line:\n")
print(file.readline())
print(file.readline())
print(file.readline())
print("-"*50)
file.close()

# readlines(): reads the file line by line, returns a list of lines
file = open(path)
print(file.readlines())
file.close()