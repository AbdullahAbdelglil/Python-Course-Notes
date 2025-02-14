#------------------------
# Problem statement: 
# given user email, u asked to extract the user name, domain
# Example: abdullah@gmail.com --> username= abdullah, domain= .com
#------------------------


def slice(email):
    email.strip()
    idx = email.index("@")
    username = email[:idx]
    domain = email[idx+1:]

    return f"username: {username}\ndomain: {domain}"