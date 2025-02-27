# ------- Writing in file --------
# 1- write("txt"): this is the used method in writing operations
# 
# 2- writelines(list[Strings]): write all the list content in the selected file.
#
# 3- close(): close the file after each operation (Best Paractice)
#
# important notes: 
# 1- write mood: override the old file content.
# 2- to create new line u must ad \n at the end of the string, 
# because the write method dosn't add it automatically.
# 3- append mood: modifey the old content and add the new text to the file, dosn't delete the old file content.
# -----------------------------

# Lets check note number 1:
# 1- open file and write in it, then close
# 2- read it, then close
# 3- repete step 1
# 4- repete step 2

# 1- open file and write in it, then close
file_path = r"C:\Users\Abdullah.Zaky\Desktop\Python-Course-Notes\Topics\File-Handling\abdullah.txt"

myfile = open(file_path, 'w')
myfile.write("Hello from python language")
myfile.close()

# 2- read it, then close
myfile = open(file_path)
print(myfile.read())
print("-"*50)
myfile.close()

# 3- repete step 1
myfile = open(file_path, 'w')
myfile.write("File content are changed by abdullah zaky")
myfile.close()

# 4- repete step 2
myfile = open(file_path)
print(myfile.read())
print("-"*50)
myfile.close()

# Lets try append mood
myfile = open(file_path, 'a')
myfile.write("\ntrying append mood, and check if it replace the old content or no !")
myfile.close()

# read it
myfile = open(file_path)
print(myfile.read())
print("-"*50)
myfile.close()

# ----- Important Notes -----
# 1- tell(): this method return the position of the cursor in ur file.
# 2- new line in any os = 2 bytes => \r\n so its calculated as 2 chars
# 3- seek(position): move the cursor to the specified position to read from there.

# Lets try: 
# ---------------------------

# 1- tell()
myfile = open(file_path)
print(myfile.tell()) #: tell = 0 if mode is 'reed'
print("-"*50)
myfile.close()

myfile = open(file_path, 'a')
print(myfile.tell()) # cursor starts for the last char in the file = 110
print("-"*50)
myfile.close()

# 2- seek()
myfile = open(file_path)
myfile.seek(5)
print(myfile.read())