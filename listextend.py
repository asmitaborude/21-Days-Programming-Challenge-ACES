#python list extend()
#Example 1: Using extend() Method
# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List:', language)

#Example 2: Add Elements of Tuple and Set to List
# language list
language = ['French']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
language.extend(language_tuple)

print('New Language List:', language)

# appending language_set elements to language
language.extend(language_set)

print('Newer Language List:', language)

#other extend methods
#1. the + operator

a = [1, 2]
b = [3, 4]

a += b    # a = a + b
print('a =', a)

#2. the list slicing syntax

a = [1, 2]
b = [3, 4]

a[len(a):] = b
print('a =', a)