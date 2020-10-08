#Example 1: Reverse a List
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)

#Example 2: Reverse a List Using Slicing Operator
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list
#Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)

#Example 3: Accessing Elements in Reversed Order

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)