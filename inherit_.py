


# defines parent class of User
class User:  
    f_name = 'Provide name'
    l_name = 'Wilson'
    email = 'JohnWilson@gmail.coms'


# defines child sub-class of User for Teacher
class Teacher(User):
    # additional attributes for Teacher sub-class
    college = True
    degree = ' '
    department = 'Science'


# defines child sub-class of User for Student
class Student(User):
    # additional attributes for Student sub-class
    gender = ' '
    grade_level = ' '
    gpa = ' '


"""
    Method that is called when object created for a class.
    Allows class to initialize the attributes of a class. 
"""

def __init__(self, f_name, l_name, email): 
    self.firstname = f_name
    self.lastname = l_name
    self.email = email

   
