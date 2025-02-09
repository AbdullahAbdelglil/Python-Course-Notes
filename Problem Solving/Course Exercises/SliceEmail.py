#------------------------
# Problem statement: 
# given user email, u asked to extract the user name, domain
# Example: abdullah@gmail.com --> username= abdullah, domain= .com
#------------------------

email = input("please enter ur email: ").strip()
idx = email.index("@")
username = email[:idx]
domain = email[idx+1:]

print(f"username: {username}\ndomain: {domain}")