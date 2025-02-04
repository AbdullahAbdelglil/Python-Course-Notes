#-------- Numbers ---------
#
# Python supports three types of numbers: integers, floating point, and complex numbers.
# They are defined as int, float, and complex class in Python.
# U can convert int, float to any type with the int(), float(), and complex() methods.
# U can't convert complex numbers into another number type.
# Python also has a random() method to generate a random number.
# -------------------------
# - Arithmetic Operations -
# Addition (+)
# Subtraction (-)
# Multiplication (*) 
# Division (/) - always returns a float
# Modulus (%) - remainder of the division
# Exponentiation (**) - raise to the power of
# Floor division (//) - returns the integer part of the division
# -------------------------

# Integers
a = 1
b = 35656222554887711
c = -3255522
d = 0

print(type(a))
print(type(b))
print(type(c))
print(type(d)) 

print(float(a))
print(complex(b))
# -------------------------

# Float
a = 1.10
b = 1.0
c = -35.59
d = 0.98

print(type(a))
print(type(b))
print(type(c))
print(type(d)) 
print(int(c))
print(complex(b))
# -------------------------

# Complex
a = 3+5j
b = 5j
c = -5j
print(type(a))
print(type(b))
print(type(c))
print("Real part of a: {}, imaginary part of a: {}" .format(a.real, a.imag))
print("Real part of b: {}, imaginary part of b: {}" .format(b.real, b.imag))
# -------------------------

# Random Number
import random
print(random.randrange(1, 10))
# -------------------------

# Arithmetic Operations
x = 10
y = 3
addition = x + y
addition1 = x + -y
subtraction = x - y
subtraction1 = -x - y
subtraction2 = -x - -y
multiplication = x * y
division = x / y
modulus = y % x
exponentiation = x ** y
floor_division = x // y

print("addition: ", addition)
print("addition1: ", addition1)
print("subtraction: ", subtraction)
print("subtraction1: ", subtraction1)
print("subtraction2: ", subtraction2)
print("multiplication: ", multiplication)
print("division: {:.2f}" .format(division))
print("modulus: {:.2f}" .format(modulus))
print("exponentiation: ", exponentiation)
print("floor_division: ", floor_division)
# -------------------------