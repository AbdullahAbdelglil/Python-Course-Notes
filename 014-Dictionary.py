# --------- Dictionary ---------
# 1- Dict items are enclosed in curly braces
# 2- Dict items are consists of key : value
# 3- Dict key must be immutable : number, string, tuple, (list not allowed)
# 4- Dict value may be any data type
# 5- Dict key must be unique, if u repeated it, it will override the old value.
# 6- Dict not ordered, means u cant use index to get an item
# 7- u can use len() method to get the number of items inside the dict
# Bonus: Dict and json object are the same in the most.
# ------------------------------

# Declaration: contains any possible values, including nested dict.
employee= {
    "name": "Abdullah",
    "age": 23,
    "gender": "male",
    "languages": ["python", "java", "c++"],
    "rate": 8.8,
    "projects": {
        "EMS" : {
            "features":15,
            "fixed_issues":10,
            "total_tasks":25
        },
        "RFID" : {
            "features":2,
            "fixed_issues":0,
            "total_tasks":2
        }
    },
    "soft_skills":("Team working", "Time management", "Adaptability")
}

# print the employee
print("dict: ", employee)

# Get a specific item form the dict:

name_1 = employee["name"]
name_2 = employee.get("name")

print(f"approach one: {name_1}\napproach two: {name_2}")

# Dealing with objects like list, tuple, and dict
languages_list = employee["languages"]
soft_skills_tuple = employee["soft_skills"]
projects_nested_dict = employee["projects"]

print(f"""
languages_list: {languages_list}
soft_skills_tuple: {soft_skills_tuple}
projects_nested_dict: {projects_nested_dict}
""" )

# Accessing items inside list, tuple, and dict
first_language = languages_list[0]
second_project = projects_nested_dict["RFID"]
third_skill = soft_skills_tuple[2]

print(f"""
first_language: {first_language}
second_project: {second_project}
third_skill: {third_skill}
""" )

# U can use keys() and values() methods to get a list of keys and values of the dict
keys = employee.keys()
values = employee.values()

print(f"keys: {keys}\nvalues: {values}")