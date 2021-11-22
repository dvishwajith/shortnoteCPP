#!/usr/bin/env python3

class Employee:
    'Common base for employee'
    employee_count = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.employee_count = Employee.employee_count + 1

    def displayCount(self):
        print("Total Employee count is %d" % Employee.employee_count)

    def displauEmplyee(self):
        print("Employee name :", self.name, " Emplyee salary", self.salary)

    def __del__(self):
        print("%s is about to be destroyed" % self.__class__.__name__)


emp1 = Employee("Syler", 1000)
emp2 = Employee("Sachin", 200)
emp1.displauEmplyee()
emp2.displauEmplyee()

print("Total employees are ", emp2.employee_count)
print("2nd method Total employees are ", Employee.employee_count)


print("""
# setiing . checking deleting attributes
""")


emp1.age = 7
print(" hasattr(emp1, 'age') ", hasattr(emp1, 'age'))
print(" hasattr(emp2, 'age') ", hasattr(emp2, 'age'))

print(" getattr(emp1, 'age') ", getattr(emp1, 'age'))
print(" setattr(emp2, 'age', 8) ", setattr(emp2, 'age', 8))
print(" delattr(emp1, 'age') ", delattr(emp1, 'age'))

print("""
# Built in functions
""")

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

del emp1
print("deleted emp1. Just before that __del__(this) functio will be called automatically")

################ Grabage Collection ############################

#       a = 40      # Create object <40>
#       b = a       # Increase ref. count  of <40> 
#       c = [b]     # Increase ref. count  of <40> 
#       
#       del a       # Decrease ref. count  of <40>
#       b = 100     # Decrease ref. count  of <40> 
#       c[0] = -1   # Decrease ref. count  of <40> 

print("""
# Inheritance
""")


class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


print("""
# You can see that __init__() does not call super class contructor automatically
You have to call it by your self
""")


class Parent2():
    'parent to show inheritance with superclass iniitalisation'
    parentAttr = 100

    def __init__(self) -> None:
        print("Calling parent contructor")
    
    def parentMethod(self):
        print("Calling parentMethod")

    def setAttr(self, val):
        Parent2.parentAttr = val

    def getAttr(self):
        return Parent2.parentAttr


class Child2(Parent2):
    'parent to show inheritance with superclass iniitalisation'

    def __init__(self) -> None:
        super().__init__()
        print("Calling child contructor")
    
    def childMethod(self):
        print("Calling ChildMethod")
        

c = Child2()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



print("""
# Operator overloading
""")

class Vector():
    '2d vecotr'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(self.x) + "," + str(self.y)


a = Vector(4, 5)
b = Vector(2, 3)
c = a + b
print("c = a + b -> c ", c)


print("""
# Data hiding
""")


class JustCounterClass:
    'Just counter to demo data hiding'
    __secret_counter = 0
    
    def __init__(self):
        JustCounterClass.__secret_counter = JustCounterClass.__secret_counter + 1
        print("JustCounterClass.__secret_counter ", JustCounterClass.__secret_counter)


CountDemo = JustCounterClass()
CountDemo2 = JustCounterClass()

# print("CountDemo.__secret_counter", CountDemo.__secret_counter)   #This will giveen error

print("__ just add _ClassName and renamve the varialbe. It can be accessed read . But not write to it")
print("CountDemo.JustCounterClass__secret_counter", CountDemo._JustCounterClass__secret_counter)

# JustCounterClass.JustCounterClass__secret_counter = 10 This will not work


print("CountDemo.JustCounterClass__secret_counter = 3 ", CountDemo._JustCounterClass__secret_counter)

print("In this exampel we use a static varialbe. But you can make a class member variable private too")


""" 
Operator            Expression	Internally
Addition            p1 + p2	    p1.__add__(p2)
Subtraction         p1 - p2	    p1.__sub__(p2)
Multiplication      p1 * p2	    p1.__mul__(p2)
Power               p1 ** p2	p1.__pow__(p2)
Division            p1 / p2	    p1.__truediv__(p2)
Floor Division	    p1 // p2	p1.__floordiv__(p2)
Remainder modulo)	p1 % p2	    p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	        p1 & p2	    p1.__and__(p2)
Bitwise OR	        p1 | p2	    p1.__or__(p2)
Bitwise XOR	        p1 ^ p2	    p1.__xor__(p2)
Bitwise NOT	        ~p1	        p1.__invert__()

 """