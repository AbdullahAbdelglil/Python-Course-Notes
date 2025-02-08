# ------ Control Flow ------
#   -- If , ElIf, Else --
# syntax: if Condition :
                # flow ..
# syntax: elif Condition :
                # flow ..
# syntax: else :
                # flow ..
# --------------------------

name  = input("Please enter your name: ")
age = int( input("Please enter your age: ") )
gender = input("Please enter your gender: ")

if gender == "m":
    if age >= 18:
        print(f"Hello mr {name}")
    else:
        print(f"Hello my bro{name}")

elif gender == "f":
    if age >= 18:
        print(f"Hello madam {name}")
    else:
        print(f"Hello mrs {name}")

else:
    print(f"Hello beskletta {name}")
# --------------------------

# u can use (and, or) operators for complex logical conditions
# --------------------------