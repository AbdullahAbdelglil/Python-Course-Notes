# ------ Date and Time handling ------
# There is a module for dealing with data andd time in python known as datetime
# ------------------------------------

import datetime as dt

# Pritn current date time
print("Current datetime = ", dt.datetime.now())

# Pritn current Year
print("Current year = ", dt.datetime.now().year)

# Pritn current month
print("Current month = ", dt.datetime.now().month)

# Pritn current day
print("Current day = ", dt.datetime.now().day)
print("-"*25)

# Print only current time
print("current time = ", dt.datetime.now().time())

# Print only current hour
print("current hour = ", dt.datetime.now().time().hour)

# Print only current minute
print("current minute = ", dt.datetime.now().time().minute)

# Print only current second
print("current second = ", dt.datetime.now().time().second)
print("-"*25)

# Print only current date
print("current date = ", dt.datetime.now().date())

# Print only current year
print("current date = ", dt.datetime.now().date().year)

# Print only current month
print("current date = ", dt.datetime.now().date().month)

# Print only current day
print("current date = ", dt.datetime.now().date().day)
print("-"*25)

# You have also method time to dealing only with time, and date method for date.

# Print the smallest possible time
print("The zero hour of ur day = ", dt.time.min) 

# Print the greatest possible time
print("The final microsecond fo your day = ", dt.time.max) 
print("-"*25)

# Print the smallest possible date
print("The smallest date = ", dt.date.min) 

# Print the greatest possible time
print("The greatest date = ", dt.date.max)  
print("-"*25)

# how you can get a specific date ? use datetiem() constructor.
# Year, month, day are mandatory to datetime() constructor.

print("my birth date = ", dt.datetime(2002, 5, 13))
print("my birth date full data= ", dt.datetime(2002, 5, 13, 4, 30, 15))
print("-"*25)

# Are we able to subtract 2 dates for any purpose ? like calculating the age using the birthdate?
# Yes u can but it is sooo complex, just use '-' operator between the 2 dates.

myBirthDay = dt.datetime(2002, 5, 13, 4, 30, 15)
currentDateTiem = dt.datetime.now()

myAge = currentDateTiem - myBirthDay
print("I lived for", myAge)
print(f"I lived for {myAge.days} Days.")
print("-"*25)

# ------ Date Time Formatting ------
# how i can format the datatime ?
# use the strftiem() method from datetime
# this method accepts the format u want.
# to know more about this formats visit: https://strftime.org/
# ----------------------------------

myBirthDay = dt.datetime(2002, 5, 13,)
print("formated date: ", myBirthDay.strftime("%d/%m/%Y"))
print("Month of birth: ", myBirthDay.strftime("%B"))
print("Month of birth: ", myBirthDay.strftime("%b"))
print("Day of birth: ", myBirthDay.strftime("%A"))
print("Day of birth: ", myBirthDay.strftime("%a"))
print("-"*25)
