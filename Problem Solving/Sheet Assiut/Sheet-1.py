# A. Say Hello
''' name = input()
print(f"Hello, {name}")
print("-"*50) '''

# ---------------------------

# B. Basic Data Types
''' line = input()
dataTypes = line.split()
for i in range(len(dataTypes)):
    print(dataTypes[i]) '''
    
# ---------------------------

# C. Simple Calculator
''' line = (input()).split()

x= int(line[0])
y= int(line[1])

print(f"{x} + {y} = {x+y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} - {y} = {x-y}") '''

# ---------------------------

# D. Difference
''' line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

a *= b
c *= d

print(f"Difference = {a-c}") '''

# ---------------------------

# E. Area of a Circle
''' pi = 3.141592653
r = float(input())
area = pi * r**2
print("%.9f" % (area)) '''

# ---------------------------

# F. Digits Summation
''' line = input().split()
a = int(line[0])%10
b = int(line[1])%10

print(a+b) '''

# ---------------------------

# G. Summation from 1 to N
''' n = int(input())
summation = (n * (n+1)) // 2
print(summation) '''

# ---------------------------

# H. Two numbers
''' line = input().split()
a = int(line[0])
b = int(line[1])
floating_number = a/b
floor = a//b
float_part = floating_number-floor

if floating_number == floor: ceil = floor
else: ceil = floor+1

if float_part>=0.5: round = ceil
else:  round = floor

print(f"floor {a} / {b} = {floor}")
print(f"ceil {a} / {b} = {ceil}")
print(f"round {a} / {b} = {round}") '''

# ---------------------------

# I. Welcome for you with Conditions
''' line = input().split()
a = int(line[0])
b = int(line[1])

if a>= b: print("Yes")
else: print("No") '''

# ---------------------------

# J. Multiples
''' line = input().split()
a = int(line[0])
b = int(line[1])
mx = max(a,b)
mn = min(a,b)
if mx % mn == 0 : print ("Multiples")
else: print("No Multiples") '''

# ---------------------------

# K. Max and Min
''' line = input().split()
nums = list(map(int, line))

mx = max(nums)
mn = min(nums)

print(f"{mn} {mx}") '''

# ---------------------------

# L. The Brothers
''' name1 = input().split()
name2 = input().split()

if (name1[1] == name2[1]): print("ARE Brothers")
else: print("NOT") '''

# ---------------------------

# M. Capital or Small or Digit
letter = input()

if letter.isalpha():
    print("ALPHA")
    
    if letter.isupper(): print("IS CAPITAL")
    else: print("IS SMALL")
    
elif letter.isdigit(): print("IS DIGIT")