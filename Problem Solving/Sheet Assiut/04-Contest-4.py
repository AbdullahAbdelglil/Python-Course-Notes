# A. Timon and Pumbaa
""" a, b = map(int, input().split())
if a>=b:
    print(a-b)
else: 
    print(0) """
# ---------------------------

# B. Drawing 'X'
""" n = int(input())
grid = [['*' for _ in range(n)] for _ in range(n)]

r, l = 0, n-1
i = 0
cr, cl = '\\', '/'
while i<n:
    grid[i][r] = cr
    grid[i][l] = cl
    r+=1
    l-=1
    i+=1
grid[n//2][n//2] = 'X'
    
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end="")
    print() """
# ---------------------------

# C. Finding Minimums: there is an error in slicing
from functools import reduce
 
    
n, k = map(int, input().split()) 
pure_k = k
nums = list(map(int, input().split()))
if k == 1:
    for i in nums:
        print(i, end=" ")
else:
    start = 0
    while k<=n:
        slc = nums[start:k] 
        start+=pure_k
        k+=k
        print(reduce(min, slc), end=" ")
    if(start<n): print(reduce(min, nums[start:]))