#!/usr/bin/env python3

def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("After function")
    return wrapper


def sayWhee():
    print("whee")

sayWhee = my_decorator(sayWhee)

print(
'''
sayWhee = my_decorator(sayWhee)
This is same as  

@my_decorator
def sayWhee():
    print("whee")

'''
)

@my_decorator
def SayBlah():
    print("Say blah")


SayBlah()

print('''
Variadia argument Decorator
''')

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return wrapper

@do_twice
def sayHello(name):
    print("hello ", name)

sayHello("Vishwa")



def print_args(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        func(*args, **kwargs)
    return wrapper

@print_args
def functionWithINputs(a, b, test):
    print("Inside functionWithINputs", a, b, test)


functionWithINputs(1, 2, "testing variadic inputs print")


print('''
Order of calling decorators
''')

@do_twice
@print_args
def OrderCheckFnction(a, b):
    print("Insode OrderCheckFnction ", a, b)


OrderCheckFnction(1, 2)

print('''
Different Order of calling decorators
''')

@print_args
@do_twice
def DiffereneOrderCheckFnction(a, b):
    print("Insode DiffereneOrderCheckFnction ", a, b)


DiffereneOrderCheckFnction(5,6)