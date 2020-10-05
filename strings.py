name = input('Enter your name: ')
print ("Who's github profile is this? ")
print('This is ' + name + "'s github profile")

#formatted strings
name = 'Asmita'
college = 'DYPCOE'
#message = name + '[' + college + '] is a student'
msg = f'{name} [{college}] is a student.'
#print(message)
print(msg)

#calculate length of a string
#we cannot calculate length of integer
print("length of this string is: " + str(len(msg)))
#print string in upper case letters
print(msg.upper())
#print string in lower case letters
print(msg.lower())