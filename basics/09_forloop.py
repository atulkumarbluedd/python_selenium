for i in 1,2,3,4,5:
    print('python')
    print(i)

print('**************************************************************')
num=[1,2,3,23,32]
for val in num:
    print(val)

print('*************************dictionary iteration*************************************')

score={'Hindi':80,
       'English':90,
       'Science':89,
       'marathi':50}

for subject, marks in score.items():
    print(f'subject is {subject}')
    print(f'marks is {marks}')

# we wanted only keys

for keys in score.keys():
    print(keys)
for values in score.values():
    print(values)
# print 1 to 1000
for num in range(1,11):
    print(num)






