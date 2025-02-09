#------------------------
# Problem statement: 
# given a user age, u asked to print the age in years, months, days, and hours
# Example: age=36 --> months = 36*12 , days = months * 30, hours = days*24
#------------------------

age = int(input("please enter ur age: ")).strip()
months = age * 12
weeks = months * 4
days = months * 30
hours = days * 24
minutes = hours * 60
print(f"month\'s: {months}\nweek\'s: {weeks}\nday\'s: {days}\nhour\'s: {hours}\nminute\'s: {minutes}")
