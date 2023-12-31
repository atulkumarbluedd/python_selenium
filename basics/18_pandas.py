import pandas

data = pandas.read_csv('test.csv')
# # print(data)
# # print only salary collumn
# print(data.salary)
# # find min and max salary
# print(f'{data.salary.min()} --> min salary')
# print(data[data.id == 105])
# max_salary=data.salary.max()
# print(f'{data[data.salary==max_salary]} --> data of emp. with max salary') # print the data of emply with max salary
#
# # find the total and average salary of employee
#
# print(f'{data.salary.mean()} --> total avg salary of employees')

# data_103_emp=data[data.id==103]
# print(data_103_emp)
# print(f'{}-> combined fist name and last name')
# print(data_103_emp.firstname.values[0],data_103_emp.lastname.values[0]) # combined first and last name of 103 id
# print(f'{data.salary.to_list()} --> all salary in form of list')
# print(f'{data.to_dict()} --> data in dictionary format')
#
#
# # modiy data
# data.loc[data.id==103,'salary']=89900
# print(data) # but this will not be changed in the existing file

# remove data of emp
# data=data.drop(9)
# print(data)
#
# # short the salary asscending order
# data=data.sort_values(by='salary')
# print(data)
# # short sal in descending order
# data=data.sort_values(by='salary',ascending=False)
# print(data)


# provide bonus to the employee i.e add new collumn in the table
data['bonus']=data.salary*0.1
print(data)

# drop the salary collumn
data=data.drop('bonus',axis=1) # axis=1 is for collumn
print(data)


# how to do permanent changes in the file
data['bonus']=data.salary*0.1
print(data)
data.to_csv('modified_test.csv')