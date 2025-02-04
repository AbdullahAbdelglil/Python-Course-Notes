#----- the old approach ------
# ---- Using Placeholders ----
#
# 1- (%s), or (%.ns): for strings,
# where .n is the number of chars u want to print.
#
# 2- (%d) : for numbers
#
# 3- (%f), or (%.nf) : for float, 
# where .n is the number of digits after the floting point, by default it's = 6
#
# --------- Syntax ----------
# print ("string %plaseholder string %placeholder" % (value1, value2)) 
#------------------------------

name = "abdullah"
age = 23
rank = 95.555

print("Hello, my name is %.3s, im %d years old, and my rank = %.2f" % (name, age, rank))

#----- the new approach ------
# --------- using {} ---------
#
# 1- {:s}, or {:.ns}: for strings,
# where .n is the number of chars u want to print.
#
# 2- {:d} : for numbers
#
# 3- {:f}, or {:.nf} : for float, 
# where .n is the number of digits after the floting point, by default it's = 6
#
# --------- Syntax ----------
# print ("string {} number {} float {}" .format(val1, val2, val3)), or
# print ("string {:s} number {:d} float {:f}" .format(val1, val2, val3))
#------------------------------

print("Hello, my name is {}, im {} years old, and my rank = {}"  .format(name, age, rank))
print("Hello, my name is {:.4s}, im {:d} years old, and my rank = {:.1f}" .format(name, age, rank))

# Format money:

mybalance = 900560850990
print("my balance in bank = {:_}".format(mybalance))
print("my balance in bank = {:,}".format(mybalance))

# Rearrange items

firstname, midname, lastname = "Abdullah", "Abduljalil", "Zaky"
print("Full name is: {} {} {}" .format(firstname, midname, lastname)) 
print("Full name is: {2} {0} {1}" .format(firstname, midname, lastname))
print("Full name is: {2} {1} {0}" .format(firstname, midname, lastname))

# for more details about formatting, visit: pyformat.info