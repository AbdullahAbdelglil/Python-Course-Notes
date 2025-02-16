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
