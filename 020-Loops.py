# ------ While loop ------
# Syntax: while condition_is_true:
#           code statemnt
# ------------------------
t = 5
while t>0:
    print(t)
    t-=1
else: print("loop terminated.")
print("-"*25)

# note: else is optional in ur loop.
myFrinds = ["mt", "ma", "ae", "am", "sh", "ra", "sh"]

i = 0
while i<len(myFrinds):
    print(f"{i+1}: {myFrinds[i]}")
    i+=1
print("-"*25)

# ------ For loop ------
# Syntax: for item in iterable:
#           code statemnt
# ----------------------

myFrinds = ["mt", "ma", "ae", "am", "sh", "ra", "sh"]
for i in myFrinds:
    print(i)
print("loop ended")

print("-"*25)

nums = [1,2,3,4,5,6,7]
sum = 0

for i in nums:
    sum+= i
else: print(f"sum = {sum}")

print("-"*25)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
for number in nums:
    if number%2 == 0: print(f"{number} is even")
    else: print(f"{number} is odd")
print("-"*25) 

student_grades = {
    "std1": {
        "compiler": 'C',
        "Computer Arch": 'B',
        "Network": 'B+',
        "CAD":'B',
        "Security":'B'
    },
    "std2": {
        "compiler": 'B',
        "Computer Arch": 'B+',
        "Network": 'B+',
        "CAD":'A',
        "Security":'A+'
    },
    "std3": {
        "compiler": 'A+',
        "Computer Arch": 'A',
        "Network": 'B+',
        "CAD":'B',
        "Security":'B+'
    }
}

# nested loop
for student in student_grades:
    print(f"{student}: ")
    student_values = student_grades[student]
    
    for value in student_values:
        print(f"{value}: {student_grades[student][value]}")
        
    print("-"*10)

# Adanced loop in dictionary

for student, grades in student_grades.items():
    print(student)
    for course, grade in grades.items():
        print(f"{course}: {grade}")
    print("-"*10)
        

# ----------------------
# Break, Continue, Pass
# syntax: 
# continue: skip current iteration
# break: break the loop in current iteration
# pass: use when u write a function or loop or condition and not implement it yet to skip this empty line
# ----------------------

