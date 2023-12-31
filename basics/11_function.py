# default value will be used if age is not provided
def myfun(user_name, Age=20):
    print(f'welcome {user_name}')
    print(f'Age is {Age}')


# calling a function
myfun("shyam", 45)
myfun('babu rao', 56)
myfun('rohan ')


# we can provide none as well if you don't want to give default values

def myfun1(user_name, Age=None):
    print(f'welcome {user_name}')
    print(f'Age is {Age}')


myfun1("Atul")


# dynamic argument function
# use * as a list for the function -> means we can send multiple values for the single parameter

def greeting(user_name, *hobbies):
    print(f'welcome {user_name}')
    for hobby in hobbies:
        print(f'hobby is {hobby}')


greeting("atul", 'shooting', 'singing', 'dancing')

# *************************************************************************************************************************************
# dynamic argument **
print(
    '*********************************************************************************************************************')


# note > dynamic argument should be in last
# Normal variable should be before default variable

def user_detail(name, **user_info):
    print(f"Name -{name}")
    for key, value in user_info.items():
        print(f" -{key}:{value}")


user_detail("raju", age=18, city="lucknow", email="raju@8980")
user_detail("tony", age=90, salary="8009", email="tony@909")


# note > dynamic argument should be in last
# Normal variable should be before default variable

def user_detail2(name, age=30, **user_info):
    print(f"Name -{name} : age {age}")
    for key, value in user_info.items():
        print(f" -{key} : {value}")


user_detail2("radhe", 89, city="lucknow", email="radhe@8980")


# Return in function


def addition(num1, num2):
    sum = num1 + num2
    return sum


result = addition(90, 30)
print(f' addition of the numbers are :-> {addition(10, 34)}')
print(f' addition of the numbers are --> {result}')
