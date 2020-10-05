input = 'This is my github account'
#to print first letter
print(input[0])
#to print letters at negative index it consider first letter at 0 index and count from back end
print(input[-1])
#to print letter from index 0 to 2 it excludes letters at index 3
print(input[0:3])
#to print letters at all index from 0
print(input[0:])

name = 'github'
print(name[1:-1])
#to find index of a letter
print(name.find('h'))
#to replace the string with some other string
print(name.replace('github', 'This is my github account'))
#to check whether the content is from given string
print('github' in name)
print('Github' in name)
