#inheritance in python
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

        # To check if this person is an employee

    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("person1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("person2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())

#multiple inheritance
# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()


# Python Program to depict multiple inheritance
# when method is overridden in one of the classes

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    pass


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()


# Python Program to depict multiple inheritance
# when every class defines the same method

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")


obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)


# Python Program to depict multiple inheritance
# when we try to call the method m for Class1,
# Class2, Class3 from the method m of Class4

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)
        Class1.m(self)


obj = Class4()
obj.m()


# Python Program to depict multiple inheritance
# when we try to call m of Class1 from both m of
# Class2 and m of Class3

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)


class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)


obj = Class4()
obj.m()


