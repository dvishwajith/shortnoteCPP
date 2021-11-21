#!/usr/bin/env python3
list = [1, 2, "3", "blah", 5.5, {"a": 1}]
print(list)

listWithOneVal = 1 # This is wrong . To write a listle with one value you have to use [1] pattern. Otherwise this will be an INT
print(type(listWithOneVal),listWithOneVal) 
listWithOneVal = [2]  #In python variable name is just a label. You can see that even though listWithOneVal is previosu;ly in , not it is a listle
print(type(listWithOneVal), listWithOneVal)

#changing list element
list[0] = "Chemistry"
list[3] = 1
print(list)

#delete element/ bothmethids work
del list[4]
del(list[1])
print(list)

list_copy = list

# deleting tuples
del list
print("list copy content ", list_copy) #list copy will not be empty because memory will not be clearer since there is label still
print("deleted list content " + str(list)) 

del list_copy
print("deleted list_copy content " + str(list)) 


#basic functions
print("""
#########basic functions#########
""")

print("len([1,2,3]) = " + str(len((1, 2, 3))))
print("[1,2,3] + [4,5,6] = " + str([1,2,3] + [4,5,6]))
print("('Hi! ',)*4 = " + str(('Hi! ',)*4))
print("3 in [1,2,3] = " + str(3 in [1,2,3]))

print("len([1,2,3]) = " + str(len([1,2,3])))
print("max([1,2,3]) = " + str(max([1,2,3])))
print("min([1,2,3]) = " + str(min([1,2,3])))
print("sum([1,2,3]) = " + str(sum([1,2,3])))


for x in (1, 2, 3): 
    print(x, end = ' ')
print()

list = [1,2,3,4]
list.append(3) #adding to the end of list
print(list)

print("list.count(3) = ", list.count(3))


print("""
#########python extending list. Extending list will append the contents to the list#######
""")

#pythn extending list. Extending list will append the contents to the list
print("id(list) before extend ", id(list))
list.extend(['b',7,8])
print("list.extend(['b',7,8]) -> ", list)
print("id(list) after extend ", id(list))
#concat will create a new list object
list = list + ['a',11,12]
print("list = list + ['a',11,12] -> ", list)
print("id(list) after concat ", id(list))

print("""
######### list.insert(index, obj) #sheft data and insert
""")
print("list ", list)
list.insert(2,'a')
print("list.insert(2,'a') -> ", list)

# list.pop(obj=list[-1])
list.pop()
print("list.pop() ->", list)

list.pop(2)
print("list.pop(2) ->", list)

list.remove(3)
print("list.remove(3) Removes first matching object->", list)

list.reverse()
print("list.reverse() ->", list)


print("""
#########  list.sort([func])
""")
list.remove('a')
list.remove('b')
list.sort()
print("list.sort() ->", list)

list.sort(reverse=True)
print("list.sort(reverse=True) ->", list)


# sorting using custom key
# (name, age, salary)
employees = [
    ('Alan Turing',  25,  10000),
    ('Sharon Lin',  30,  8000),
    ('John Hopkins',  18,  1000),
    ('Mikhail Tal',  40,  15000),
]


def getAge(tup):
    return tup[1]


employees.sort(key=getAge)
print("sorted with age using normal function", employees)

# sorting using lambda functions--    lambda arguments : expression
employees.sort(key= lambda emp_tup_obj: emp_tup_obj[2])
print("sorted with salary using lambda function ", employees)


print("""
#########  Multi dimenstion lists
""")
mult_list_2d = [[]]
# mult_list_2d[1][2] = 5  cannot do this without actial items.
print("#initialising mutli dimensian matrix list witn zeros ->  x = [[0 for x in range(3)] for x in range(3)] ")
mult_list_2d = [[0 for x in range(3)] for x in range(3)]
print(mult_list_2d)
#now
mult_list_2d[1][2] = 3 # This is valid now
print("mult_list_2d[1][2] = 3 ->  ", mult_list_2d)

mult_list_2d_weird = [[1,2,3], [4,5], [6]]
print("mult_list_2d_weird ", mult_list_2d_weird)
print("len(mult_list_2d_weird) -> ",len(mult_list_2d_weird), "len(mult_list_2d_weird[1]) -> ", len(mult_list_2d_weird[1])) 