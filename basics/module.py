import calcy;
import employees_class

result = calcy.myfun("atul", 90)

# object is created !!
emp1 = employees_class.Employees('Raju', "raju@gmail.com", "Sales", 50000)
print(emp1.name + f': name')
print(f'{emp1.salary} : salary')
print(emp1.dept + f' : dept')
print(emp1.email + f' : email')

# another way to call
print('*********** !! another way to call via object !! ***********************')
emp2 = employees_class.Employees('sohan', 'sohan@gmail.com', 'HR', 100000)
emp2.emp_info()
emp1.emp_info()

# how to change the data of the perticular employee !!
emp2.change_dept("devops")
emp2.emp_info()

# another way to call class level variables this value will be common for all the objects
print(emp1.COMPANY)
print(employees_class.Employees.COMPANY)
print(emp1.name)
