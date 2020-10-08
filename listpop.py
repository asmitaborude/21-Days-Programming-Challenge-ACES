#Example 1: Pop item at the given index from the list
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

#Example 2: pop() without an index, and for negative indices
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)