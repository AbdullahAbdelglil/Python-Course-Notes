# ------ Class methods ------
# 1- Class method marked with @classmethod decorator to mark it as a class method
# 2- It take Cls(class) to point to the class
# 3- It dosn't require object instantiation to use it
# 4- Difference between Class method and instance method:
#    instance methods: its functionality depends on the instance
#    so its output varies based on the instance attributes, but the class methods
#    depends not depends on the instance attribute, and its behaviour is the same 
#    for all instances.
# ---------------------------

class Employee:
    
    # Class attributes
    company_ceo = "Abdullah Abduljalil"
    num_of_employees = 0
    
    def __init__ (this, name, dept, manager, salary):
        
        #Instance attributes
        this.name = name
        this.dept = dept
        this.manager = manager
        this.salary = salary
        Employee.num_of_employees+=1

    def get_emp_info(this):
        return f"name: {this.name}, dept: {this.dept}, manager: {this.manager}, salary: {this.salary}"
    
    @classmethod
    def get_comp_ceo(Cls):
        return Cls.company_ceo

    @classmethod
    def get_emp_count(Cls):
        return Cls.num_of_employees

    @staticmethod
    def connect_to_database():
        print("database connected successfully")

print(Employee.get_emp_count())

emp1 = Employee("Ahmed", "frontend", "bechoy", "30000$")
emp2 = Employee("kariem", "backend", "agbo", "50000$")
print(emp1.get_emp_info())
print(emp2.get_emp_info())

print(Employee.get_emp_count())

# u can access the class method by instance
print("CEO: ", emp1.get_comp_ceo())

# ---------------------------
# Static methods:
# 1- dosn't force u to pass a parameter, in other words:
# not like instance or class method that force u to add at least one parameter (self, or cls)
#
# 2- Its a class level method, dont realted to the instance
# 3- marked with @staticmethod decorator
# 4- we use it to perform any tasks that not related to the class or the instance,
#    like connecting to the database, integerate with 3rd party service and so on ..
# 5- we can access it as same as the classmethod
# ---------------------------

