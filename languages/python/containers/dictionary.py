#!/usr/bin/env python3

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 7:'testintkey', 1.5:'testfloatkey', (1,1.5):'testTuplekey'}
print(dict)

# if you define values with same keys they will be replaces . for example key 7 here
dict_2 = {'Name': 'Amir', 'Age': 8, 'Class': 'First', 7:'testintkey', 1.5:'testfloatkey', (1,1.5):'testTuplekey', 7:[1,2,3]} 
print(dict_2)

del dict_2[7] # This delete en entry with key name 7
dict_2.clear() # clea all the element s in the dicitonary
del dict_2 #this delete athe entire dictionary


dict_3 = {'Name': 'Amir', 'Age': 8, 'Class': 'First', 7:'testintkey', 1.5:'testfloatkey', (1,1.5):'testTuplekey', 7:[1,2,3]} 
print(" 'Name' in dict3 = ", 'Name' in dict_3)

print("dict_3.items() -> ", dict_3.items()) # returns dicitonary (key, item) tuple pairs
print("dict_3.keys() -> ", dict_3.keys()) # returns dict keys
print("dict_3.values() -> ", dict_3.values()) # return all items

dict_3.update(dict)
print("dict_3.update(dict) This will add dict into dict3 -> ", dict_3)

# dict4 = dict + dict_3 This is not valid

print("""
Class object as hash Keys
""")

class A():
   def __init__(self, data=''):
       self.data = data  

   def __str__(self):
       return str(self.data)

d = {}  
obj = A()  
d[obj] = 'abc'  
print("d[obj] = ", d[obj])
obj2 = A()
d[obj2] = "cdf"
print("d[obj2] = ", d[obj2])    # KeyError  because elem2 is not elem. 
# The  __hash__() gives different outputs. if you want this to be valid override the __hash__() function
# to get the has using input string data

print("""
Sorting accoring to values
""")
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("input x dictonary", x)
X_sorted_by_vales_tuples = sorted(x.items(), key=lambda item: item[1])  #lamdbda function extract value
print("X_sorted_by_vales_tuples ",X_sorted_by_vales_tuples)

X_sorted_by_vales_dictionary = {k: val for k, val in sorted(x.items(), key=lambda item: item[1])}
print("X_sorted_by_vales_dictionary ",X_sorted_by_vales_dictionary)


print("""
Sorting accoring to Keys
""")
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("input x dictonary", x)
X_sorted_by_keys_tuples = sorted(x.items(), key=lambda item: item[0]) #lamdbda function extract key
print("X_sorted_by_keys_tuples ",X_sorted_by_keys_tuples)

X_sorted_by_keys_dictionary = {k: val for k, val in sorted(x.items(), key=lambda item: item[0])}
print("X_sorted_by_keys_dictionary ",X_sorted_by_keys_dictionary)