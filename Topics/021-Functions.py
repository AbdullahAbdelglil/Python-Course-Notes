# ------ Fucntions ------
# Syntax: def function_name(param1, param2, ..):
#               block of code
#               return data
# -----------------------

def check_numbers(a, b): 
    if type(a) != int or type(b) != int:
        print("only integers allowed")
        return 0
    else: return 1

def summation(a, b):
    if(check_numbers(a, b)): return a+b
    else: return 0
    
def subtraction(a, b):
    if(check_numbers(a, b)): return a-b
    else: return 0

def multiplication(a, b):
    if(check_numbers(a, b)): return a*b
    else: return 0

def division(a, b):
    if(check_numbers(a, b)): return a/b
    else: return 0

def exponent(a, b):
    if(check_numbers(a, b)): return a**b
    else: return 0

def calculator(a, b, operations):
    sum = 0 
    sub = 0
    mul = 0
    div = 0
    expo = 0
    
    if "sum" in operations:
        sum = summation(a,b)
    if "sub" in operations:
        sub = subtraction(a,b)
    if "mul" in operations:
        mul = multiplication(a,b)
    if "div" in operations:
        div = division(a,b)
    if "expo" in operations:
        expo = exponent(a,b)
        
    return sum, sub, mul, div, expo

sum, sub, mul, div, expo = calculator(4, 2, ["sum", "sub", "mul", "div", "expo"]) 

print("sum = ",sum)
print("sub = ",sub)
print("mul = ",mul)
print("div = ",div)
print("expo = ",expo)
print("-"*50)
#----------------------------------------------

# --- Packing and Unpacking (*Argument) ----
# the idea of packing is make the function more general
# let's take an example: the old summation() method can apply the summation'
# only on two parameters. now what if we dont know the number of parameters ?
# we can use a list of numbers in the function parameter, or use *
# * means, apply the function on these arguments, number of them dosn't matter
# ------------------------------------------

# this is the idea of packing
def summation(*numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum

print(summation(1,2,3,4,5,6))
print(summation(1,2,3))
print(summation(1,2,3,4))
print(summation(1))
print("-"*50)
# note: the number of arguments dosn't matter

# the idea of unpacking: 
# if the function return more than one value, 
# i don't know the number of them, or the order

def summation(*numbers):
    sum = 0
    sub = 0
    mul = 1
    for num in numbers:
        sum+=num
        sub-=num
        mul*=num
    return mul, sum, sub

# unpaking:
values = summation(1,2,3,4)
print(values)
print("-"*50)
#----------------------------------------------

# ------ Default parameters -------
# u can put a default values for parameters
# lets take an example: when u developed the exponent function
# u need to put a default value for the exponent, even if user
# forget to write it, it will add the default value and perform the function without error
# ---------------------------------

# addign a default value for b
def exponent(a, b=1):
    if(check_numbers(a, b)): return a**b
    else: return 0

exp1 = exponent(5)
exp2 = exponent(5, 2)

print(exp1, exp2)
print("-"*50)
# but not: if u add a defult value for a parameter, 
# u must add a default value for all the next parameters in the function
# say: hello(name1, name2, name3):
# if u add a default for num1, u must add to num2, num3
# and so on, if u add for num2, u must add to num3.
#----------------------------------------------


# --- Packing and Unpacking (**KWArg) ----
# in the previous appoach for paking using (*args)
# the function will read args as a tuple, what if we want to pass a dict ?
# to pass a dict, use **args
# lets take an example
# ----------------------------------------

# paking using *
def show_skills(*skills):
    print(type(skills))
    
    for skill in skills:
        print(skill) 
    
show_skills("html", "css", "js")
print("-"*50)
# paking using **

def show_skills_with_progress(**skills):
    print(type(skills))
    
    for skill, progress in skills.items():
        print(f"{skill} => {progress}") 
    
show_skills_with_progress(html = "80%", css = "80%", js = "90%")
print("-"*50)
# u can pass the dict itself like this:
skills = {
    'html': 80,
    'css' : 70, 
    'js' : 60
}

show_skills_with_progress(**skills)
print("-"*50)
# lets take an example that compine all together: paking, unpaking *, **, and default value

def print_cv(name, *languages, **skills):
    print(f"Hello {name} Yor languages is: ")
    for lang in languages:
        print(lang)
    print("And Your Skills is: ")
    for skill, prog in skills.items():
        print(f"{skill} : {prog}")
    
print_cv("Abdullah", "Java", "C++", "Pyhton", html = "70%", css = "60%", js= "50%")
print("-"*50)
# also u can define the languages tuple, and skills dict, then pass them as args

languges = ("Java", "C++", "Pyhton")
skills ={
    'html': "70%", 
    'css': "60%", 
    'js': "50%"
}

print_cv("Ahmed", *languges, **skills)
print("-"*50)
# note: u can ignore paking the tuple using (*), but u cant do this with dict, 
# (**) is must for unpaking

# ----------------------------------------

# Function Scope in python like functio scope in any programming language
# but there is a trick in python: if u want to override a global object 
# inside a function, u can do it in python using global keyword before the variable 
# lets take an example:
# ----------------------------------------

x = 1
def first():
    x = 2 
    print(f"x form the function scope= {x}")


first()
print(f"x form the global scope= {x}")
print("-"*50)
# what if we override the global variable inside the function

def second():
    global x 
    x = 4
    print(f"x form the function scope= {x}")


second()
print(f"x form the global scope= {x}")
print("-"*50)

# ----------------------------------------
# ------------ Lambda Function -----------
# 1- Lambda has no name 
# 2- u can call it inline, without defining it
# 3- Lambda used for simple functions, not recommended for large tasks
# 4- Lambda is one single expression, not block of code
# syntax: var =  lambda parameters : line of code
# to use it, just call: var(args)
# ----------------------------------------

welcom = lambda name, age : print(f"Hello mr {name}, your age is {age}")
welcom("abdullah", 23)
print("-"*50)