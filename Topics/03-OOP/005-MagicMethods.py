# ------ Magic methods or Dunder method ------
# 1- Magic methods (also called dunder methods, short for double underscore) 
# in Python are special methods that start and end with double underscores (__). 
# They define how objects of a class behave with built-in operations 
# like arithmetic, comparison, iteration, and more.
# 
# What is the meaning of "They define how objects of a class behave with built-in operations" ?
# lets descus a problem: now what if u want to use str() built-in method to print the
# content of emp1 ? lets try
# --------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

emp1 = Employee("Abdullah", "10")
print(str(emp1))
print("-"*50)
# this will be the output: <__main__.Employee object at 0x000002B1F36F8A50>

# Magic methods comes in here to help us: 
# u can use __str__(self) and write in it the behaviour of the str() method u want.

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
    def __str__(self):
        return f"name: {self.name}\nsalary: {self.salary}"

emp1 = Employee("Abduljalil", "15")
print(str(emp1))
print("-"*50)

# u can also add the behaviour u want in the magic methods, 
# u can write how to add 2 emps using __add__(emp1 ,emp2) 
# and use (+) operator to perform object addetion, and so on..

print(dir(emp1))