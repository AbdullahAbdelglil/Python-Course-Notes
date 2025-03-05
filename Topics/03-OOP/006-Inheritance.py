# ------ Inheritance ------
# Intheritance is known, but how we can implement it in python ?
# Inheritance implemenetation: class childClass(MainClass):
# -------------------------

class Animal:
    def __init__(self, sound, action, food):
        self.sound = sound
        self.action = action
        self.food = food
        
    def __str__(self):
        return f"Animal:\ntype: {self.type}\nsound: {self.sound}\naction: {self.action}\nfood: {self.food}"

class Dog(Animal):
    def __init__(self, type, sound, action, food):
        super().__init__(sound, action, food)
        self.type = type

# ------ Multiple Inheritance ------
# Important thing to know: python supports multiple inheritance
# The child class can inherit form more than one class
# How pyhton handles the multiple inheritance ? 
#   python uses something called the C3 Linearization algorithm 
#   to determine the method resolution order (MRO).
# Lets take an example:
# ----------------------------------

class A:
    def greet(self):
        print("hello Form A")

class B(A):
    def greet(self):
        print("hello Form B")

class C(A):
    def greet(self):
        print("hello Form C")

class D(B, C):
    pass

d = D()
d.greet() 

# it will calls B.greet() because
# the first class listed in parentheses has higher priority 
# when determining the Method Resolution Order (MRO)
# The MRO follows depth-first, left-to-right order, while avoiding duplicate method calls.
