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