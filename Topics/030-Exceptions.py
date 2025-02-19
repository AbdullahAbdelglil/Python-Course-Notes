# ------ Exceptions in Python ------
# 1- To know more about python built-in exceptions, visit this link: 
# https://docs.python.org/3.12/library/exceptions.html
# 
# 2- to raise ur own exception, follow this syntax:
# raise Exception(your_message)
# ----------------------------------

# Lets paly

def factorial(number):
    """
    main role: calculatuing the factorial of any number > 0
    Alert: dont bass any number less than 0, it will raises an error
    """
    if (number<1):
        raise Exception(f"Number must be graeter than 0, {number} is not.")
    else:
        f = 1
        for i in range(2, number+1):
            f*=i
        return f

# print the documintation for the function, or module
""" print(help(factorial))

f5 = factorial(5)
print(f5)
f_mius_5 = factorial(-5)
print(f_mius_5) """

# You can specify the type of exception u want to raise.
def sum(num1, num2):
    if num1 != int or num2 != int:
        raise ValueError("Only integer values are allowed for adding")
    else: return num1+num2
    
""" s1 = sum(5, 10)
print(s1)
s2 = sum(5, "10")
print(s1) """
# -----------------------------------

# ------- Exception Handling --------
# -- try | except | else | finally --
# -----------------------------------
# Try, Except: like try, catch in java.
# Esle: if no error, do something
# Finally: if there is an error or no, do something 
# the block code in finally block must run, like closing resources.
# ------------------------------------
# Lets take an example: we will try open 2 files, and write from one to the other
# so: two files must be exist, if there any one doesn't be exist, tell him
# after this: if one is opend, u must close it
# syntax:


second_file = open(r"C:\Users\EGYPT SOFT\Desktop\Python-Course-Notes\Topics\014-Dictionary.py", mode="a")
try:
    first_file = open("\Decorators.py", mode= "r") # not exist file
     # exist
    
    line = first_file.readline()
    second_file.write(line)
except FileNotFoundError:
    print("first_file dosn't exists, check ur path.")
finally: # close the opend file anyway.
    second_file.close()