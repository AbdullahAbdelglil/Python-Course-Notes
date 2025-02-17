# ------ Decorators ------
# 1- A decorator is a special function that allows you to modify or enhance
# another function without changing its code directly.
#
# 2- In Python, functions are first-class objects, meaning they can be passed as arguments to other functions. 
# Decorators take advantage of this by wrapping a function inside another function.
#
# 4- Decorators are commonly used for things like logging,
# caching, and measuring execution time.
# 
# 5- U can use more than one decorator up on the same function
#
# Lets see how we can create a decorator and use it
# Example: craete a decorator that measuring execution time of a the function that calculate the fact of number
# ------------------------

# 1- Basic syntax:
import time as t

def timer(func):
    def wrapper(number) :
        start_time = t.time()
        result = func(number)
        end_time = t.time()
        print(f"The total Execution Time = {end_time - start_time} ms")
        return result
    return wrapper

@timer
def get_factorial(number):
    factorial = 1
    for i in range(2, number+1):
        factorial*=i
    return factorial

num = 5
fact = get_factorial(num)
print(f"Factorial of {num} =", end =" ")
print(fact)
print("-"*25)

# 1- Create the decorator func
# 2- Create the wrapper function inside the decorator
# 3- add the new functionality and call the wanted method (factorial in our example)
# 4- return the value of the method (factorial)
# 5- return the wrapper method from decorator
# 6- add @decorator_name above the wanted method (factorial in our example)
# note: we add @decorator above the method impl, not calling.
# ------------------------

# lets create another decorator for adding separator after each print statement

def separator(func):
    def wrapper(txt):
        func(txt)
        print("-"*25)
    return wrapper

@separator
def custom_print(txt):
    print(txt)
    
custom_print("Hello under decorator")