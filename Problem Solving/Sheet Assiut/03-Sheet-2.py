# A. 1 to N
# n = int(input())
# for i in range(1, n+1):
#     print(i)
# -------------------------

# B. Even Numbers
# n = int(input())
# if n<2:
#     print(-1)
# else:
#     for i in range(2, n+1, 2): print(i)
# -------------------------

# C. Even, Odd, Positive and Negative
# n = int(input())
# even = 0
# odd = 0
# positive = 0
# negative = 0
# nums = list(map(int, input().split()))
# for i in range(n):
#     num = nums[i]
#     if num%2 == 0 :
#         even+=1
#     else:
#         odd+=1
#     if num>0:
#         positive+=1
#     elif num<0:
#         negative+=1
#
# print("Even: ", even)
# print("Odd: ", odd)
# print("Positive: ", positive)
# print("Negative: ", negative)
# -------------------------

# D. Fixed Password

# password = input()
# while password != "1999":
#     print("Wrong")
#     password = input()
# else: print("Correct")
# -------------------------

# E. Max
# max_num = -1
# n= int(input())
# nums = list(map(int, input().split()))
# for i in range(n):
#     num = nums[i]
#     max_num = max(max_num, num)
# print(max_num)
# -------------------------

# F. Multiplication table
# n = int(input())
# for i in range(1, 13):
#     print(f"{n} * {i} = {n*i}")
# -------------------------

# G. Factorial
# n = int(input())
# def factorial(num):
#     fact = 1
#     for i in range(num, 0, -1):
#         fact*=i
#     return fact
#
# for i in range(n):
#     num = int(input())
#     print(factorial(num))
# -------------------------

# H. One Prime
# number = int(input())
# r = number//2
# for i in range(r, 1, -1):
#     if number % i == 0:
#         print("NO")
#         break
# else: print("YES")
# -------------------------

# I. Palindrome
""" number = input()
reversed_number = int(number[::-1])

print(reversed_number)
if number == str(reversed_number):
    print("YES")
else:
    print("NO")
 """
# -------------------------

# J. Primes from 1 to n
""" def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [1] * (n + 1)

    for num in range(2, int(n**0.5) + 1):  
        if is_prime[num]:  
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = 0

    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

n = int(input())
primes = sieve_of_eratosthenes(n)
for i in range(len(primes)):
    print(primes[i], end =" ") """
# -------------------------

# K. Divisors
''' def get_divisors(number): 
    divisors = [1,number]
    for i in range(2, int(number**.5)+1):
        if number%i == 0:
            divisors.append(i)
            div = number//i
            if(div != i): divisors.append(div)

    divisors.sort()
    return divisors
    
number = int(input())
divisors = get_divisors(number)
for i in range(len(divisors)):
    print(divisors[i])  '''
# -------------------------

# L. GCD

# My solution:
''' 
nums = list (map(int, input().split()))
n1 = nums[0]
n2 = nums[1]
min_num = min(n1, n2)
max_num = max(n1, n2)

divisors = get_divisors(min_num)
divisors = divisors[::-1]

for i in range(len(divisors)):
    num = divisors[i]
    if max_num % num == 0:
        print(num)
        break
    
# The best solution (Euclidean algorithm):
# there is a mathematical property:
# while a>b : gcd(a,b) = gcd(b, a%b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

nums = list(map(int, input().split()))
n1 = nums[0]
n2 = nums[1]
min_num = min(n1, n2)
max_num = max(n1, n2)
print(gcd(max_num, min_num)) '''
# -------------------------

# M. Lucky Numbers
''' lr = list (map(int, input().split()))

lucky = 0
for i in range(lr[0], lr[1]+1):
    counter = 0
    num_str = str(i)
    for c in num_str:
        if c== "4" or c== "7":
            counter +=1
            
    if counter == len(num_str) : 
        lucky=1
        print(i, end=" ")
    
if lucky == 0 :  print(-1) '''
# -------------------------    

# N. Numbers Histogram
''' symbol = input()
n = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    print(symbol*i) '''
# -------------------------    

# O. Pyramid
''' n = int(input())
i = 1
while i<=n:
    print("*"*i)
    i+=1 '''
# -------------------------

# P. Shape1
''' n = int(input())
while n>0:
    print("*"*n)
    n-=1 '''
# -------------------------

# Q. Digits
''' n = int(input())
while n>0:
    number = input()
    number = number[::-1]
    for c in number:
        print(c, end=" ")
    print()
    n-=1 '''
# -------------------------

# R. Sequence of Numbers and Sum
''' while True:
    line = list(map(int, input().split()))
    n1 = line[0]
    n2 = line[1]
    if n1<=0 or n2<=0:
        break
    sum = 0
    for i in range(min(n1,n2), max(n1,n2)+1):
        print(i, end=" ")
        sum+=i
    print(f"sum ={sum}") '''

# -------------------------

# S. Sum of Consecutive Odd Numbers
''' n = int(input())
while n:
    line = list(map(int, input().split()))
    n1 = line[0]
    n2 = line[1] 
    odd_sum = 0
    if n1%2: odd_sum-=n1
    if n2%2: odd_sum-=n2
    for i in range(min(n1,n2), max(n1,n2)+1):
        if i%2: 
            odd_sum+=i
    print(odd_sum)
    n-=1 '''
# -------------------------

# T. Shape2
''' n = int(input())
i=1
size = (n*2)-1
pyramid = [[' ']*size]*n

idx = 0
l = size//2
r = l+1
while idx<n:
    for i in range(l, r):
        pyramid[idx][i] = '*'
    for i in range(0, r):
        print(pyramid[idx][i], end="")
    print()
    idx+=1
    l-=1
    r+=1 '''
# -------------------------

# U. Some Sums
''' line = list(map(int, input().split()))
n = line[0]
a = line[1] 
b = line[2] 

def get_sum_of_digits(num):
    sum = 0
    while num:
        sum+=num%10
        num//=10
    return sum

total_sum = 0
for i in range(1, n+1):
    sod = get_sum_of_digits(i)
    if(sod>= a and sod <= b): 
        total_sum += i
print(total_sum) '''
# -------------------------

# V. PUM
''' n = int(input())
i = 1
while n:
    c  = 3
    while c:
        print(i, end=" ")
        i+=1
        c-=1
    print("PUM")
    i+=1
    n-=1 '''
# -------------------------

# W. Shape3 
''' n = int(input())

def draw_pyramid(n):
    size = (n*2)-1
    pyramid = [[' ' for _ in range(size)] for _ in range(n)]

    idx = 0
    l = size//2
    r = l+1
    while idx<n:
        for i in range(l, r):
            pyramid[idx][i] = '*'
        idx+=1
        l-=1
        r+=1
    return pyramid

pyramid = draw_pyramid(n)
reversed_pyramid = pyramid[::-1]

def print_pyramid(pyramid, n, is_reversed=0):
    if is_reversed : r = (n*2)-1
    else: r=n
    for i in range(len(pyramid)):
        line = pyramid[i]
        for j in range(0, r):
            print(line[j], end="")
        print()
        if is_reversed : r-=1
        else: r+=1


print_pyramid(pyramid, n)
print_pyramid(reversed_pyramid, n, 1) '''
# -------------------------

# X. Convert To Decimal 2
''' n = int(input())
while n:
    number = int(input())
    bin_rep = bin(number)
    ones = ""
    for c in str(bin_rep):
        if c == "1":
            ones+="1"
    print(int(ones, 2))
    n-=1 '''
# -------------------------

# Y. Easy Fibonacci

''' n = int(input())
f1 = 0
f2 = 1
print(f1, end=" ")

if n>=2: 
    print(f2, end=" ")
    i=3
    while i<=n:
        f = f1+f2
        print(f, end=" ")
        f1 = f2
        f2 = f
        i+=1 '''
# -------------------------

# Z. Three Numbers -> wrong answer
# basic solution: 3 nested loops o(n*3), but unfortunetly, its not me...
# i wanna extract an equation for solving it in O(1).
line = list(map(int, input().split()))
k = line[0]
s = line[1]
counter = 0
for i in range(0, k+1):
    for j in range(0, k+1):
        l = s-(i+j)
        if l>=0 and l+i+j==s:
            counter+=1
               

print(counter)

''' if s<=k:
    print(((s+1)*(s+2))//2)
else:
    m = s//3
    if k < m: 
        print(0)
    elif k == m:
        print(1) # its right for here
 '''    ''' else:
        k-=m
        k+=1
        print((k*6)-3) '''


