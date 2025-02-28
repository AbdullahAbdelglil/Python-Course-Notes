# ------ Class Syntax & Info ------
# 1- Class defined with (class) keyword
# 2- Class name written in CamleCase (like java)
# 3- Syntax:

class Car:
    
    # Constructor
    def __init__(self, brand, model, color, price):
        # Instance attributes: changes based on the user arguments.
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    
# Lets Break it down: 
# 1- class: the python keyword for creating a class
# 2- class name: must written in CamleCase 
# 3- __init__(): the constructor of the class
# 4- any method starts and ends with __ called a Dunder or magic method
# 5- __init__(): the method that directly called automatically once u instanstiate an obejct form ur class
# 6- self parameter: referes to the current instance, must be the first param in __init__()
# like (this) keyword in java, just the only different: u can change it ot any word u wnat.
# 7- in Python u dont need to call new() method to instancite an obejct
# 8- Instance atrributes written in the constructor

g_class_car = Car("Mercedes", "G35", "Black", 15)
bmw_car = Car("BMW", "520i", "Dark Blue", 7)

# Print instance attribute
print(g_class_car.model)
print(bmw_car.model)
# Note: each instance has its own model (instance attribute)