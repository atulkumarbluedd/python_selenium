print("hello")
# this is to print formatting the code is specific format !!
print(f"the sum is {10 + 20} ")
"""
 this is to print formatting the code is specific format !!
 this is to print formatting the code is specific format !!
"""

user_list=["raju","shyam","paul","ron","grave"]
print(user_list[0])
# add item into list
user_list.append('gorilla')
# delete value from list
user_list.remove("raju")
# modify the existing values
user_list[2]='Gorilla'
print(user_list)
# insert at specific index
user_list.insert(1,'shanu')
print(user_list)

# del lists
# del user_list;
# print(user_list) # error we will get user_list' is not defined
# delete at specific index
del user_list[1]
print(user_list)

print(len(user_list))

# sorting
user_list.sort();
print(user_list)
user_list.sort(reverse=True)
print(user_list)

# delete last element from list
lastvalue=user_list.pop();
print(lastvalue)
# delete specific index
print(user_list.pop(2))

user_list=["raju","shyam","paul","ron","grave"]
print(user_list[0:3])
# or
print(user_list[:3])
# getting last two values
print(user_list[-2:])

#****************************************** numeric list *********************

nums=[89,90,78]
print(nums)
print(min(nums))
print(sum(nums))

mix_lists=['paul',89,90,90.0] # allowed any type of values
print(mix_lists)

copy_mixList=mix_lists;

copy_mixList.append('s')
print(copy_mixList)
# using copy method to copy list

copy_1=mix_lists.copy()
print(copy_1)
