str="hello brother"
str3="bro"

print(str[1])
 # substring
print(str[0:4])
# print all except last two chars from last

print(str[0:-2])

# how to check whether string present inside another string or not
print(str3 in str)
print(str.split(" ")) # splitting the string via spaces
print("hell ".strip()+"::") # remove spces from the end
print(" hello".lstrip()) # left strip
print("hello ".strip()) # right strip
