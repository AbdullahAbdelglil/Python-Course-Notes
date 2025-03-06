# -------- Polymorphism ---------
# Polymorphism is one of the four fundamental principles of OOP, 
# alongside Encapsulation, Abstraction, and Inheritance. 
# It allows objects of different classes to be treated as objects of a common superclass, 
# making code more flexible and scalable.
# The term "polymorphism" is derived from Greek, meaning "many forms." 
# In programming, it refers to the ability of a function, method, or operator to 
# behave differently based on the object that calls it.
# Polymorphism allows a single interface to represent different types (or classes), 
# enabling code reusability and flexibility.
# -------------------------------

# ---- Types of Polymorphism ----
# Polymorphism is broadly classified into two main types:
# 1- Compile-time Polymorphism (Static Polymorphism):
#   - This type of polymorphism is resolved during compilation.
#   - It is achieved through method overloading and operator overloading.
#
# 2- Runtime Polymorphism (Dynamic Polymorphism)
#   - This type of polymorphism is resolved at runtime.
#   - It is achieved through method overriding (also called "Dynamic Method Dispatch").
#   - The actual method that gets called depends on the object type, not the reference type.
# -------------------------------


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    # To achive the method abstraction
    def print_car_info(self):
        raise NotImplementedError("print_car_info method must be implemented")

class Proche(Car):
    def __init__(self, model, price):
        super().__init__(model, price)
    def print_car_info(self):
        print(f"Model: {self.model}, Price= {self.price}")

my_car = Proche("Macan", "4.5M")
my_car.print_car_info()