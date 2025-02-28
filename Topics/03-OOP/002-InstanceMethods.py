# ------ Instance method ------
# 1- Instance method: like any method u create it, but..
# Instance method must take the (self) as a parameter
# 2- it can access all instance attributes
# 3- also it can access the class attributes

class Student:
    
    university = "Al-azhar"
    
    def __init__(this, first_name, last_name, grade, GPA):
        this.first_name = first_name
        this.last_name = last_name
        this.grade = grade
        this.GPA = GPA
    
    def print_info(this):
        print(f"Student name: {this.first_name} {this.last_name}")
        print(f"Student University: {Student.university}")
        print(f"Student grade: {this.grade}")
        print(f"Student GPA: {this.GPA}")
    
student1 = Student("Abdullah", "Abduljalil", "4", "3.3")
student1.print_info()