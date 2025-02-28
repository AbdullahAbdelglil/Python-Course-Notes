# C. Finding Minimums

''' from functools import reduce

n, k = map(int, input().split())
arr = list(map(int, input().split()))
p1, p2 = 0, k
while(True):
    if(p2>=n): 
        m = reduce(min, arr[p1:])
        print(m, end=" ")
        break
    
    m = reduce(min, arr[p1:p2])
    print(m, end=" ")
    p1 = p2
    p2 += k '''
# -------------------------------

# D. Range Sum
''' n = int(input())
while(n>0):
    l, r = map(int, input().split())
    mn = min(l, r)
    mx = max(l, r)
    
    sum1 = (mn*(mn+1))//2
    sum2 = (mx*(mx+1))//2
    
    print(abs(sum2-sum1+mn))
    n-=1 '''
# -------------------------------

# E. Hady Rides the Train
''' id = int(input())
row = id//4
if(row%2==0):
    col = id%4
else:
    col = 3-id%4

print(f"{row} {col}") '''
# -------------------------------

# F. Break Number

''' def Fx(num):
    counter = 0
    f_part = 0
    while(f_part==0):
        if(num%2==0): 
            counter+=1
        else: break
        f_part = num/2 - num//2
        num//=2
    return counter
    
n = int(input())
nums = list(map(int, input().split()))
max_count = 0
for num in nums:
    max_count = max(Fx(num), max_count)

print(max_count) '''
# -------------------------------

# G. Construct the Sum
''' t = int(input())
while t:
    n, s = map(int, input().split())

    # Check if it's impossible to construct the sum
    if (n * (n + 1)) // 2 < s:
        print(-1)
    else:
        result = []
        sum_so_far = 0

        # Start picking numbers from n down to 1
        for i in range(n, 0, -1):
            if sum_so_far + i <= s:
                result.append(i)
                sum_so_far += i

            if sum_so_far == s:
                break

        print(*result)

    t -= 1 '''
# -------------------------------

# H. Simple Mod
n = int(input())
print("0 0")
