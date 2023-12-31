try:
    print(10 / 0)
except ZeroDivisionError:
    print('kindly do not devide by zero !!')

print(10 + 2)

# ***********************if exception does not occured then execute else don't execute ************************

try:
    with open('tr.in','r') as file:
        content = file.readlines()
except FileNotFoundError:
    print("file is not present. please provide a file which exists")
else:
    for lines in content:
        print(f' Welcome {lines.strip()}')



# *********************************** how to write a generic exception ************************************************

try:
    with open('tr.in','r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    for lines in content:
        print(f' Welcome {lines.strip()}')
finally:
    print(" i will be executed at any cost as i am finally")


