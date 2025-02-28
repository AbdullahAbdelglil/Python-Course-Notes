# ------ Class Attributes & Methods ------
# The difference between class (attrs & methods) and Instance (attrs & methods) is:
#
# 1- instance attributes changes from one instance to another, but class attributes is not
#    class attribute is the same for all class instances
#
# 2- to access an instance attribute: instance_name.attribute
#    to access a class attributes: ClassName.attribute
# ----------------------------------------

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
        return this.name, this.dept, this.manager, this.salary
    