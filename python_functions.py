#Python Functions
#Example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))

#Scope and Lifetime Variables
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

#Python Function Arguments
#Variable Function Arguments
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

#Python Arbitrary Arguments
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")

#Python Recursion
#Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

#Python anonymous/Lambda Function
#Example of Lambda Function in python

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

#Python global, local, non-local
#Create a Global Variable
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

# Create a Local Variable

def foo():
    y = "local"
    print(y)

foo()

#Using Global and Local variables in the same code
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

#Create a nonlocal variable
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

#Python Global Keyword
#Accessing global Variable From Inside a Function
c = 1 # global variable

def add():
    print(c)

add()

# Changing Global Variable From Inside a Function using global
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)




