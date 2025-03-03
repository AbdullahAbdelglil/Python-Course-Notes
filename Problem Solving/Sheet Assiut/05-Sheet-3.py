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