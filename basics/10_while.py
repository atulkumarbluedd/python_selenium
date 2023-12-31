i = 0;
while i <= 10:
    print(i)
    i = i + 1

# write a prog. if user provides input as integer else quit
# user_input = ''
# while user_input != 'q':
#     user_input=input('please enter a number or press q for quit -')
#     if user_input.isdigit():
#         if int(user_input) % 2 != 0:
#             print('number is odd !!')
#         else:
#             print('number is even !!')

# break and continue

num=[23,89,90,88,5,78]

for n in num:
    if n==90:
        continue
    print(n)