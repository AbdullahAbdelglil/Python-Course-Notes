#------------------------------
# To know the role of function: just hoover on it and read the descritopn.
# 1- len(object): returns the count of items in the object
#------------------------------

# strip(), rstrip(), lstrip(): 
a = "    Abdullah     "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

print("------------------------")

a = "@@@@Abdullah@@@@"
print(a.strip("@"))
print(a.rstrip("@"))
print(a.lstrip("@"))

print("------------------------")

a = "@,#Abdullah@"
print(a.strip("@,#"))
print(a.rstrip("@,#"))
print(a.lstrip("@,#"))
#------------------------------

# title(), capitalize()
b = "abdullah abduljalil - 22 - male"
print(b.title())
print(b.capitalize())
#------------------------------

# zfill(width)
c, d, e = "1", "11", "111";
print(c)
print(d)
print(e)

print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
#------------------------------

# upper()
f = "Abdullah"
print(f.upper())
#------------------------------

# lower()
g = "Abdullah"
print(f.lower())
#------------------------------

# split("separator", maxSplit) & rsplit()
h = "i love python and java"
print(h.split())

h = "i-love-python-and-java"
print(h.split())

h = "i-love-python-and-java"
print(h.split("-"))

h = "i-love-python-and-java"
print(h.split("-", 2))

h = "i-love-python-and-java"
print(h.rsplit("-", 2))
#------------------------------

# center(width, fillChar), rjust(width, fillChar), ljust(width, fillChar)
i = "osama"
print(i.center(15, "-"))
print(i.rjust(5, "#"))
print(i.ljust(5, "~"))
#------------------------------

# count("word", startIdx, endIdx): start, end = 0, n; by default
j = "abdullah abduljalil zaky abduljalil"
print(j.count("abduljalil"))
#------------------------------

# swapcase()
k = "i love pyTHoN"
print(k.swapcase())
#------------------------------

# startswith(), endswith()
l = "Abdullah"
print(l.startswith("A"))
print(l.startswith("Ab"))
print(l.endswith("H"))
#------------------------------

# index(substr, start, end), find(substr, start, end)
# the only one difference: if the substr not found:
# index() returns an error
# find() retruns -1
m = "abdullah zaky"
print(m.index("z"))
print(m.find("z"))

print(m.find("c"))
#print(m.index("c"))
#------------------------------

# splitlines()
n = """
first line
second line
third line
"""
print(n.splitlines())

n = "first line\nsecond line\nthird line"
print(n.splitlines())
#------------------------------

#expandtabs(number of spaces u need)
o = "first name\tsecond name\tfull name"
print(o.expandtabs(5))
#------------------------------

# istitle(""), 
# isspace(" "), 
# islower(), 
# isupper(), 
# isidentifier(), 
# isalpha(), 
# isalnum()
# all of these functions return true or false, u can them for checking anything in ur string.
#------------------------------

# replace(oldValue, newValue, count)

p = "I lave my mam"
print(p.replace("a", "o", 1))
#------------------------------

# join(iterable): iterable is list or tuple
q = ["Abdullah", "Abduljalil", "Zaky"]
print(" ".join(q))
print("-".join(q))
print(", ".join(q))
#------------------------------
