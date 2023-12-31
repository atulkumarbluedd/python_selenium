print("hello")

a = 3.4

print("{} {}".format("value is", a))
print(type(a))
# data types
# list same as array of java
# tupple
val={4:3,"name":"sam"}
# print(val["name"])
val["key2"]="d"

print(val)

greeting="morning1"
if greeting =="morning":
    print("condition matches")
else :
    print("consdition not matched")

val=[2,3,5,6]
for i in val:
    print(i)
# sum of first 5 natural numbers
print("sum of first 5 natural numbers")
summation=0
for i in range(1,6):
   summation=summation+i
   if i==5:
    print(summation)

# approach 2
print("Approach 2")
summation=0
for i in range(1,6):
    summation = summation + i
print(summation)

# how to do i+=2 in for loop
# so in range give third argument as 2
print("****do i= i+2 ******")
for i in range(1,10,2):
    print(i)

# if you dont give first argument then it will start from zero and till that value excluded
print("*************skipping first argument in range function ***************")
for m in range(9):
    print(m)

def GreatMe(name):
      print("lets start with function "+name)

    # function call
GreatMe("Atul Arya")

# function with return value
print(" function with return value")
def sumOfnumber(a, b):
    return a+b
print(sumOfnumber(3,5))
