my_sets={'mon','tue','wed'}

# it is unordered unique
print(my_sets)
# even if you add intentionally duplicate value but it will not print
my_sets={'mon','tue','wed','wed'}
print(my_sets)

my_sets.add('thu')
print(my_sets)
my_sets.add('thu')
print(my_sets) # nothing will print

# convert list into set to remove duplicates
my_list=['mon','tue','wed','wed','mon','tue','wed','wed']
days_set=set(my_list)
print(days_set)

