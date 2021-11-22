#!/usr/bin/env python3

def func(a,b):
    a = 4
    b = 5

def func_str(str):
    # str[0] = 'a' This cannot be done 
    str = "bla bla" # This will only chang on local fnction copy. Python is pass by label anyway


a = 7 
b = 8

func(a,b)
print(a,b) # you can see that variables does not change

c_str = "test"
func_str(c_str)
print(c_str) # you can see that strings does not change


print("""
    Nest functons defintions and function as a return object
""")

# IN python function can define functions
# In python function can return functions

def parent(mom_or_dad):
    def printMom():
        print("I am mom")

    def printDad():
        print("I am Dad")

    if mom_or_dad == 0:
        return printMom
    else:
        return printDad


parentEvalFunc = parent(0)

print("parentEvalFunc = parent(0) and exeucting parentEvalFunc() ")
parentEvalFunc()