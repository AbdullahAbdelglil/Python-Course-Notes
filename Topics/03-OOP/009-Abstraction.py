# ------ Abstraction ------
# Abstraction is one of the four main pillars of (OOP) along with Encapsulation, Inheritance, and Polymorphism. 
# It is the concept of hiding implementation details and exposing only the necessary parts to the user.
# Think of it as focusing on "what" an object does rather than "how" it does it.
# -------------------------

# ---- How achive it ? ----
# 1- Your base class must inherit form ABC (Abstract Base Class) class
# 2- The abstracted method must decorated with @abstractmethod
# -------------------------
from abc import ABC, abstractmethod
class Car(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

# As you know:
# 1- if u skip the implementation of the abstract method, it will raise an error
# 2- You cant instantiate an object from an abstract class

class BMW(Car):
    
    def start_engine(self):
        print("Car engine started")
    
    
    def stop_engine(self):
        print("Car engine stoped")


bmw_340i = BMW()
