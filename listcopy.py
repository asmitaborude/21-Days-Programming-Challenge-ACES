#Example 1: Copying a List
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)

#Example 2: Copy List Using Slicing Syntax
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)