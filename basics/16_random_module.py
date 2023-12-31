# her we will work on random module
import random

# generate random float number b/w 0 and 1
random_float = random.random()
print(random_float)
print(random.randint(0, 10))  # generate random int b/w 0 to 10
print(random.uniform(3.5, 6.5))  # it will generate dobles b/w provided range

options = ['papaya', 'apple', 'orange', 'kiwi', 'banana', 'pears']
print(random.choice(options))
# shuffle list

random.shuffle(options)
print(" after suffling the list")
print(options)
