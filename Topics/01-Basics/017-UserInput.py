# ------ User Input ------
# to get an input from user: use input(message)
# input(): returns string
# ------------------------

abdullah = {}
name = input("please enter ur name: ")
email = input("please enter ur email: ")
age = input("please enter ur age: ")
languages = input("please enter ur skills: ")

abdullah["name"] = name
print(type(name))
abdullah["email"] = email
print(type(email))
abdullah["age"] = age
print(type(age))
abdullah["languages"] = languages
print(type(languages))

print(abdullah)

# note: all output prompts executes after input prompt