class Employees:
    # class is a blueprint or template for creating the objects and it defines the structure and behaviour of that objects.
    # object is an instance of a class. with its own unique data and the ability to perform actions

    COMPANY = 'ABC.pvt.ltd'

    # same as constructor in java
    def __init__(self, name, email, dept, salary):
        self.name = name
        self.email = email
        self.dept = dept
        self.salary = salary
        print('constructor called')

    def emp_info(self):
        print(self.name)
        print(self.email)
        print(self.salary)
        print(self.dept)

    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f'dept is changed to {new_dept}')

