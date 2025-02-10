# ------ Membership Operators ------
# 1- in
# 2- not in
#-----------------------------------

admins = ["abdullah", "tata", "Bon", "Mahmoud"]
blocked_users = ["ali", "soha", "noha"]

username = input("please enter ur user name: ").strip()

if username in admins and username not in blocked_users:
    print("hello admin")
elif username not in admins and username not in blocked_users:
    print("Hello user")
else: print("3ayez eh ya maniak ?")