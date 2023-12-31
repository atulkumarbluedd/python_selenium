marks={'Hindi':80,
       'English':90}
print(marks)
print(type(marks))
print(marks['Hindi'])
print(marks.get('Hindi'))
# if the marks are not present in the dictionary, and you dont want to get any error then use get method like below
# print(marks['jk']) # none
marks['Maths']=100
print(marks)

# delete a value
del marks['Hindi']
print(marks)
# length
print(len(marks))