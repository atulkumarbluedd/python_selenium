# if False:
#     print("hello")
#     print("brother")
# else :
#     print("lll")
#     print("my brother !!")
#
# print("please learn python !!")
# print(10==8)
#
# if 10>8:
#     print('this is true !!')
# else :
#     print('this is false !!')

users = ['paul', 'raju']

# else is not mendatory only if we also can use
if 'paul' in users:
    print('yes it is present')
else:
    print('this is not present !!')

# check if list is empty or not !
if users:
    print('list is not empty')
else:
    print('list is empty')

# ELIF
marks = int(input('please enter marks -> '))
if marks < 30:
    print('student is fail')
elif 50 > marks > 30:
    print('student has B grade')
else:
    print('student has A grade ')

# nesting
age = 29
voter_id = False
if age >= 18:
    if voter_id:
        print('yes you can vote')
    else:
        print('please apply for voter id first ')
else:
    print('you cannot vote')

# logical operators
age = 29
voter_id = False
if age >= 18 and voter_id:
    print('yes you can vote')

else:
    print('you cannot vote')

# or operator

age = 29
voter_id = False
if age >= 18 or voter_id:
    print('yes you can vote')

else:
    print('you cannot vote')
