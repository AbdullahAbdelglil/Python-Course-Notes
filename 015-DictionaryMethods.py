# --------- Dictionary Methods ---------
# 1- clear(): no thing new.
# 2- update(): add new item to ur dict
# 3- keys():
# 4- values():
# 5- setdefault({key : value})
# 6- pop("key"): delete the object form the dict, return it
# 7- popitem(): get the last added item
# 8- items(): return all items in ur dict, keys and values together. return type: list of tuples
# --------------------------------------
from conda.common.url import maybe_unquote

abdullah = {
    "name": "Abdullah",
    "age": 23,
    "gender": "Male"
}
print(abdullah)
print("-"*50)
# to add new items to ur dict u have two approaches:

# 1- using update()
abdullah.update({"status": "single", "plans":["getting PORSCHE Macan", "Getting a flat in a good place", "Getting marry from a good girl"]})
print(abdullah)
print("-"*50)
# --------------------------------------

# 2- using []
abdullah["College_grades"] =  ("good", "V.good", "good", "V.good", "Excellent")
print(abdullah)
print("-"*50)
# --------------------------------------

# setdefault(): this method look in ur dict and determine:
# if the key is found in the dict: no action,
# else: put the key:value in the dict
College_grades = abdullah.setdefault("College_grades", ("good", "Excellent"))
languages = abdullah.setdefault("languages", ["java", "python", "C++", "SQL"])
print(College_grades)
print(languages)
print(abdullah)
print("-"*50)
# --------------------------------------

# pop(): delete the object form the dict, return it
languages = abdullah.pop("languages")
print(languages)
print(abdullah)
print("-"*50)
# --------------------------------------

# items(): note, if u get the items of a dict, then u changed it, this change will reflect in items.
all_items = abdullah.items()
print("before editing the original dict", all_items)
abdullah["graduated"] = True
print("after editing the original dict", all_items)
print("-"*50)
# --------------------------------------

# cool way to construct a dict: using fromkeys(iterable, initial value)

keys = ("one", "two", "three")
initial_value = 0
my_dict = dict.fromkeys(keys, initial_value)
print(my_dict)
print("-"*50)