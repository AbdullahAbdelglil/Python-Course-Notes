# ------ Encapsulation ------
# Encapsulation is one of the four fundamental principles of OOP, 
# along with Abstraction, Inheritance, and Polymorphism. 
# It is the practice of hiding data (variables) inside a class 
# and allowing controlled access to it through methods (getters, setters).
# 
# Encapsulation means:
#   - Bundling data (fields/variables) and methods (functions) into a single unit (class).
#   - Restricting direct access to data by using private variables.
#   - Providing controlled access via getter and setter methods.
# This ensures data security, maintainability, and modularity
# ---------------------------

# ---- Access modifiers -----
# Python does not have explicit access modifiers like Java (public, protected, private).
# However, it provides conventions to indicate the accessibility of variables and methods.
# 
# Conventions:
# 1- Public: default in python
# 2- Protected: _var, _method_name
# 3- Private: __var, __method_name
#
# Python does not enforce protected, or private 
# but programmers respect it as a convention.
# 
# This means u can access the protected and privete members outside its scope 
# (but not recommended, be a good developer)
#
# Why Did Python Choose This Approach?
# Python's approach to access modifiers is not a bug or a bad thing, 
# it's just different from Java's strict enforcement.
# 
# 1- Python follows the "We are all adults here" philosophy 
# → It trusts developers to follow conventions rather than enforcing strict rules.
#
# 2- Flexibility over strict enforcement 
# → Sometimes, developers might need access to "private" variables in special cases.
#
# 3- Encapsulation is about behavior, not just access control 
# → Python promotes good coding practices instead of forcing restrictions.
# ---------------------------

class Account:
    def __init__(self, name, email, password):
        self.name = name
        self._email=email # protected member
        self.__password = password # private member
    

account = Account("Abdullah", "abdullah@gmail.com", "123")

print(account.name) # will printed because it's public
# print(account.email) # will not appers because its protected
print(account._email) # will printed (but not recommended)

# print(account.password) # will not appers because its private
# print(account.__password) # also will not appers because its private

# To access a private member: (but its not recommende, use getters and setters)
print(account._Account__password)
print("-"*50)

# --- Getters & Setters ---

class Account:
    def __init__(self, name, email, password):
        self.name = name
        self._email=email # protected member
        self.__password = password # private member
    
    def get_name(self):
        return self.name

    def get_email(self):
        return self._email
    
    def get_password(self):
        return self.__password
    
    def set_name(self, name):
        self.name = name
        
    def set_email(self, email):
        self._email = email
        
    def set_password(self, password):
        self.__password = password

account = Account("Abdullah", "abdullah@gmail.com", "123")

print(account.get_name())
print(account.get_email())
print(account.get_password())
print("-"*25)

account.set_email("abdullahzaky1@gmail.com")
print(account.get_email())