# A. Winter Sale
# Solution idea: 
# a - (a * x%) = p
# a - ax% = b
# a (1 - x%) = p
# a = b / (1-x%)

''' line = list(map(int, input().split()))
x = line [0]
p = line [1]

price_before_discount = p / (1 - (x/100))

print("%.2f" % price_before_discount) '''
# -----------------------------------

# B. Memo and Momo
''' line = list(map(int, input().split()))
a = line [0]
b = line [1]
k = line [2]

both = a%k == 0 and b%k ==0
memo = a%k == 0 and b%k !=0
momo = a%k != 0 and b%k ==0

if both:
    print("Both")
elif memo:
    print("Memo")
elif momo:
    print("Momo")
else: 
    print("No One") '''
# -----------------------------------

# C. Next Alphabet
# Solution: 
# 1- use ord(char) to get the ascii code
# 2- use chr(number) to convert the ascii to its equavilant char
''' c = input()
ascii = ord(c)
if ascii == 122 or ascii == 89:
    ascii -= 26
print(chr(ascii+1)) '''

# -----------------------------------

# D. Ali Baba and Puzzles
''' nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]
d = nums[3]

op1 = a + b - c
op2 = a + (b*c)
op3 = a - b + c
op4 = a - (b*c)
op5 = (a*b) + c
op6 = (a*b) - c

if op1 == d or op2 == d or op3 == d or op4 == d or op5 == d or op6 == d:
    print("YES")
else: 
    print ("NO") '''

# -----------------------------------

# E. Interval Sweep

''' nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]

if a == 0 and b == 0:
    print("NO")
else:
    if a==b or a-b == 1 or b-a == 1:
        print("YES")
    else: 
        print ("NO")  '''
        
# -----------------------------------

# F. Adding Bits
''' nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]

binary_a = str(bin(a)[2:].zfill(32))
binary_b = str(bin(b)[2:].zfill(32))
binary_c = [0]*32

i = -1
while i>=-32:
    a_bit = binary_a[i]
    b_bit = binary_b[i]
    
    if a_bit=="1" and b_bit=="1":
        binary_c[i] = 0
    else: 
        binary_c[i] = int(a_bit) + int(b_bit)
    i-=1

binary_string = ''.join(map(str, binary_c))
print(int(binary_string, 2)) '''

# -----------------------------------

# G. Katryoshka

''' nums = list(map(int, input().split()))
eye = nums[0]
mouth = nums[1]
body = nums[2]

if eye == 0 or body == 0:
    print(0)
elif mouth == 0:
    print (min(eye, body))
else:
    result = min(min(eye, mouth), body)
    eye-= result
    eye//= 2
    body-= result
    if eye > 0 and body>0:
        result += min(eye, body)
    print(result) '''
    
# -----------------------------------

# H. Data Type Guessing

''' nums = list(map(int, input().split()))
n = nums[0]
k = nums[1]
a = nums[2]

int_range = (-2147483648, 2147483647)
if (n*k) % a ==0:
    result = (n*k)/a
    if  result >= int_range[0] and result <=int_range[1]:
        print("int")
    else: 
        print("long long")
else:
    print("double") '''
    
# -----------------------------------

# I. Lucky Numbers

num = int(input())
d = num%10
num//=10
if d==0: print("YES")

else:
    if max(d,num) % min(d,num) == 0 :
        print("YES")
    else :
        print("NO") 