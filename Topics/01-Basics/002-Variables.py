#------------------------------
# Syntax-> <variable name> = <variable value>
#
# Naming convention and rules:
# u can start ur variable with [a-z or A-Z] or underscore (_)
# u can write in both camel case: userName, or snake case: user_name
# u can't use the variable before assign value to it.
# case-sensitive
#
# python has a reserved keywords, u can list them using: help("keywords")
#
# python is dynamically-typed language.
# it means that you don’t need to declare the type of variable when you create it,
# The type of variable is determined at runtime based on the value assigned to it.
# mn ela5er: no need to declare data types
#------------------------------

# List all the reserved keywords
help("keywords")
#------------------------------

# Dynamically-typed explaining
x=5
print(type(x))

x=[5,6,7]
print(type(x))
#------------------------------

# A cool way for assigning multiple values for multiple variables:
name,age,gender = "Abdullah", 22, "male"
# Note: number of values and variables must be equal.