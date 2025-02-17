# ------ Generators ------
# 1- Generator is a special type of iterable like list or tuple, but unlike those !
#
# 2- It doesn't store all its values in memory at once. instead, 
# it generates the values on-the-fly, one at a time, as you iterate over it.
#
# 3- U can create agenerator using a function that contains one or more yield statements.
# -------------------------

def count_up_to(num):
    counter = 1
    while counter<=num:
        yield counter
        counter+=1

counter = count_up_to(10)

# firstly lets check the type of count_up_to() function
print(type(counter)) # Generator

# Lets iterate on it:
for c in counter:
    print(c)

# the for loop calls __next()__ behind the scenes until reachs StopIteration, then break


# How the generator works ?
# -------------------------
# When a function contains a yield statement, it becomes a generator function. 
# Each time the generator's __next__() method is called, it executes the code inside the function
# until it hits the yield statement, returns the value of yield, and pauses its execution. 
# The state of the function is saved so that when __next__() is called again, it picks up right where it left off.
# -------------------------

# Some of generators use caese: 
# -------------------------
# 1- Processing large datasets: When working with large files or streams of data 
# (like reading a huge log file line-by-line).
# 
# 2- Lazy evaluation: When you only need a part of the data or don’t need to compute all the values up front, 
# such as when implementing algorithms like Fibonacci sequence or primes.
#
# 3- Pipelines: Generators are ideal when chaining together multiple operations in a pipeline, 
# especially when data needs to be processed step-by-step.