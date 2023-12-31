file = open("test") # to read file


print(file.read(5))


file.close()
# read only certain number of chars just pass
# if you want to read line by line just use readline() it will read one single line


file = open("test") # to read file

print(file.readline())


file.close()

# write a code to read file and let it end when it finds the space



file = open("test") # to read file

line=file.readline();
while(line!=""):
    print(file.readline())
    line=file.readline()
file.close()

# how to do the same in for loop
file = open("test") # to read file

for line in file.readlines():
    print(line)
file.close()