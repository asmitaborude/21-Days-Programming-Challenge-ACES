#Example 1: Working of clear() method
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)

#Example 2: Emptying the List Using del
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)