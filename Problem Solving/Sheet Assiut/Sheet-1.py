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
''' letter = input()

if letter.isalpha():
    print("ALPHA")
    
    if letter.isupper(): print("IS CAPITAL")
    else: print("IS SMALL")
    
elif letter.isdigit(): print("IS DIGIT") '''

# ---------------------------

# N. Char
''' char = input()
if char.isupper(): print(char.lower())
else: print(char.upper()) '''

# ---------------------------

# O. Calculator

''' expression = input()
addition = expression.find("+")
subtraction = expression.find("-")
multiblication = expression.find("*")
divition = expression.find("/")

def get_nums(expression, sign):
    a = int(expression[:sign])
    b = int(expression[sign+1:])
    return a,b

if addition != -1:
    a,b = get_nums(expression, addition)
    print(a+b)
elif subtraction != -1:
    a,b = get_nums(expression, subtraction)
    print(a-b)
elif multiblication != -1:
    a,b = get_nums(expression, multiblication)
    print(a*b)
elif divition != -1:
    a,b = get_nums(expression, divition)
    print(a//b) '''

# ---------------------------

# P. First digit !0
''' x = int(input()[0])
if x%2 == 0: print("EVEN")
else: print("ODD") '''

# ---------------------------

# Q. Coordinates of a Point
''' points = list(map(float, input().split()))
x = points[0]
y = points[1]

if x>0 and y>0: 
    print("Q1")
elif x<0 and y>0: 
    print("Q2")
elif x<0 and y<0: 
    print("Q3")
elif x>0 and y<0: 
    print("Q4")
elif x==0 and y==0: 
    print("Origem")
elif y==0: 
    print("Eixo X")
elif x==0: 
    print("Eixo Y") '''
    
# ---------------------------

# R. Age in Days

''' days = int(input())
years = days // 365
days -= (years * 365)
months = days // 30
days -= (months * 30)

print(f"{years} years\n{months} months\n{days} days") '''

# ---------------------------

# S. Interval
# [0,25], (25,50], (50,75], (75,100]

''' x = float(input())
if x>=0 and x <=100:
    if x<=25: print("Interval [0,25]")
    elif x<=50: print("Interval (25,50]")
    elif x<=75: print("Interval (50,75]")
    else: print("Interval (75,100]")
else: print("Out of Intervals") '''

# ---------------------------

# T. Sort Numbers
''' nums = list(map(int, input().split()))
unsorted_nums = nums.copy()
nums.sort()
for i in nums: 
    print(i)
print("")
for i in unsorted_nums: 
    print(i) '''
    
# ---------------------------

# U. Float or int
''' num = float(input())
int_part = int(num)
float_part = num - float(int_part)
if float_part == 0: print(f"int {int_part}")
else: print("float %d %f" % (int_part, float_part)) '''

# ---------------------------

# V. Comparison
''' line = input().split()
a = int(line[0])
sign = line[1]
b = int(line[2])

if sign == ">":
    if a>b: print("Right")
    else: print("Wrong")
    
elif sign == "<":
    if a<b: print("Right")
    else: print("Wrong")
    
elif sign == "=" :
    if a==b: print("Right")
    else: print("Wrong") '''
    
# ---------------------------

# W. Mathematical Expression
''' line = input().split()
a = int(line[0])
sign = line[1]
b = int(line[2])
c = int(line[4])

if sign == '+':
    if a+b == c:
        print("Yes")
    else: print(a+b)
    
elif sign == '-':
    if a-b == c:
        print("Yes")
    else: print(a-b)
    
elif sign == '*':
    if a*b == c:
        print("Yes")
    else: print(a*b) '''
    
# ---------------------------

# X. Two intervals

# 1 --------------- 15
#        5 -------------------- 27
# intersection = 5 : 15 -> x2 : y1
# there is no intersection in these cases:
# if y1 < x2 or x1 > y2
''' boundries = list(map(int, input().split()))

x1 = boundries[0]
y1 = boundries[1]

x2 = boundries[2]
y2 = boundries[3]


if y1 < x2 or x1 > y2:
    print("-1")
else:
    x = max(x1, x2)
    y = min(y1,y2)
    print(f"{x} {y}") '''
    
# ---------------------------

# Y. The last 2 digits

''' nums = list(map(int, input().split()))
mul = 1
for i in nums:
    mul*=i

out = str(mul%100)
print(out.zfill(2)) '''

# ---------------------------

# Z. Hard Compare
''' import math 

nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]
d = nums[3]

if b==1 or d ==1: 
    if a**b > c**d:
        print("YES")
    else:
        print("NO")
else:
    if b * math.log2(a) > d * math.log2(c):
        print("YES")
    else: 
        print("NO") '''