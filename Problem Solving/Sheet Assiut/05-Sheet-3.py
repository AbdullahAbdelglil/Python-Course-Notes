# A. Summation
""" n = int(input())
nums = list(map(int, input().split()))
print(abs(sum(nums))) """
# ---------------------------

# B. Searching
""" n = int(input())
nums = list(map(int, input().split()))
num = int(input())

try:
    print(nums.index(num))
except:
    print(-1) """
# ---------------------------

# C. Replacement
""" n = int(input())
nums = list(map(int, input().split()))
for i in range(len(nums)):
    if nums[i]>0:
        nums[i] = 1
    elif nums[i]<0:
        nums[i]=2
print(*nums) """
# ---------------------------

# D. Positions in array
''' n = int(input())
nums = list(map(int, input().split()))

for i in range(len(nums)):
    if(nums[i]<=10): 
        print(f"A[{i}] = {nums[i]}") '''
# ---------------------------

# E. Lowest Number
''' n = int(input())
nums = list(map(int, input().split()))
mn = min(nums)
idx = nums.index(mn)

print(f"{mn} {idx+1}") '''
# ---------------------------

# F. Reversing
''' n = int(input())
nums = list(map(int, input().split()))
nums = nums[::-1]
print(*nums) '''
# ---------------------------

# G. Palindrome Array
''' n = int(input())
nums = list(map(int, input().split()))  

if nums == nums[::-1]: 
    print("YES")
else:
    print("NO") '''
# ---------------------------

# H. Sorting
''' n = int(input())
nums = list(map(int, input().split()))  
nums.sort()
print(*nums) '''
# ---------------------------

# I. Smallest Pair
''' t = int(input())

while(t):
    n = int(input())
    nums = list(map(int, input().split())) 
    size = len(nums)
    mn = 10**12
    for i in range(size):
        for j in range(i+1, size):
            mn = min(mn, (nums[i]+nums[j]+j-i))
    print(mn)
    t-=1 '''
# ---------------------------

# J. Lucky Array
''' n = int(input())
nums = list(map(int, input().split()))  
mn = min(nums)
counter = 0
for num in nums:
    if num == mn: counter+=1
if(counter%2==0) : 
    print("Unlucky")
else:
    print("Lucky") '''
# ---------------------------

# K. Sum Digits
''' n = int(input())
num = input()
sum = 0
for i in num:
    sum+= int(i)
print(sum) '''
# ---------------------------

# L. Max Subarray

''' t = int(input())
while t:
    n = int(input())
    nums = list(map(int, input().split())) 
    size = 1
    while size<=n:
        i, j = 0, size
        while j<=n:
            sub = nums[i:j]
            print(max(sub), end=" ")
            i+=1
            j+=1
        size+=1
    print()
    t-=1 '''
# ---------------------------

# M. Replace MinMax
''' n = input()
nums = list(map(int, input().split())) 
mn = min(nums)
mx = max(nums)

for i in range(len(nums)):
    if (nums[i] == mn) : nums[i] = mx
    elif (nums[i] == mx) : nums[i] = mn
print(*nums) '''
# ---------------------------

# N. Check Code
''' a, b = map(int, (input().split()))
code = input()
symbol = code.find('-')

if symbol==a and str(code[symbol+1:]).isdigit():
    print("Yes")
else:
    print("No") '''
# ---------------------------

# O. Fibonacci
''' n = int(input())
def fib(n):
    fibonacci = [0,0,1]
    for i in range(3,n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[n]

print(fib(n)) '''
# ---------------------------

# P. Minimize Number
''' n = int(input())
nums = list(map(int, input().split()))
counter = 0
cont = True
while cont:
    count = 0
    for i in range(len(nums)):
        if nums[i]%2!=0: 
            cont = False
            break
        else: 
            count+=1
            nums[i]//=2    
    if count == len(nums): counter+=1        
print(counter) '''
# ---------------------------

# Q. Count Subarrays
''' def is_non_decreasing(sub_arr):
    i,j = 0,1
    while j < len(sub_arr):
        if sub_arr[j] < sub_arr[i]: return 0
        i+=1
        j+=1
    return 1


t = int(input())
while t:
    n = int(input())
    nums = list(map(int, input().split())) 
    size = 1
    counter = 0
    while size<=n:
        i, j = 0, size
        while j<=n:
            sub = nums[i:j]
            counter+=is_non_decreasing(sub)
            i+=1
            j+=1
        size+=1
    print(counter)
    t-=1 '''
# ---------------------------

# R. Permutation with arrays
''' n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

if  arr1==arr2: print("yes")
else: print("no") '''
# ---------------------------

# S. Search In Matrix
""" r,c = map(int, input().split())

matrix = []
for i in range(r):
    arr = list(map(int, input().split()))
    matrix.append(arr)

x = int(input())
found = False
for arr in matrix:
    try:
        arr.index(x)
        found = True
        break
    except:
        found = False

if found: 
    print("will not take number")
else: 
    print("will take number") """
# ---------------------------

# T. Matrix
""" n = int(input())
matrix = []
rdi = 0
ldi, ldj = 0,n-1
rd, ld = 0, 0

for i in range(n):
    arr = list(map(int, input().split()))
    matrix.append(arr)

while rdi<n:
    rd+= matrix[rdi][rdi]
    rdi+=1   

while ldi<n:
    ld+= matrix[ldi][ldj]
    ldi+=1   
    ldj-=1

print(abs(ld-rd)) """
# ---------------------------

# U. Is B a subsequence of A ?
A = list(map(int, input().split()))
B = list(map(int, input().split()))


for b in B:
    start = 0
    try:
        i = A.index(b, start)
    except:
        pass