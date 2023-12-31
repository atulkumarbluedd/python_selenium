# working with files

# w -> write, if file is not present then it will create new file
with open('user.txt', 'w') as file:
    file.write('This is my first file using python')

with open('user.txt', 'a') as file:
    file.write('\n added in second line')

# Read file
with open('user.txt', 'r') as file:
    content = file.read()
    print(content)
# fn readLines
with open('user.txt', 'r') as file:
    content = file.readlines()

print(' ###################################')
for line in content:
    print(line)

print(' #################To Remove The Gap in b/w the Lines ##################')

for line in content:
    print(f'Welcome {line.rstrip()}')
