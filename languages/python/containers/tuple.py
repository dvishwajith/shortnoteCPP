#!/usr/bin/env python3
tup1 = (1, 2, "3", "blah", 5.5, {"a": 1})
print(tup1)

empty_tuple = ()

tupWithOneVal = (1) # This is wrong . To write a tuple with one value you have to use (1,) pattern. Otherwise this will be an INT
print(type(tupWithOneVal),tupWithOneVal) 
tupWithOneVal = (2,)  #In python variable name is just a label. You can see that even though tupWithOneVal is previosu;ly in , not it is a tuple
print(type(tupWithOneVal), tupWithOneVal)

############ Tuples are imputalbe. That means you cannot change them#################

tupl_are_immutable = (1.1, 1, "a", "b")
###     tupl_are_immutable[1] = 0   # This is not valid. You cannot assing to a tuple like that. they are immutable

#if you want to change you can do something like this  ( or you can covert to a list and change back)
new_tuple_from_immute = tupl_are_immutable[:1] + (0, ) + tupl_are_immutable[2:] 
#can remove elemet like following
#  new_tuple_from_immute = tupl_are_immutable[:1] + tupl_are_immutable[2:] 

print(new_tuple_from_immute)
print(new_tuple_from_immute[1])  #way to access tuple objects
print(new_tuple_from_immute[1:]) # way to get all objects after 1 .  
print(new_tuple_from_immute[1:3]) # If you want in between do something like [1:3] . Not that this printing excludong index 3

# changing values by converting to lists
tupl_2_list = list(tupl_are_immutable)
tupl_2_list[1] = 100
new_tuple_from_immute_method2 = tuple(tupl_2_list)
print(new_tuple_from_immute_method2)

# deleting tuples
del new_tuple_from_immute_method2
# print(new_tuple_from_immute_method2) Thiw will gibe an error now


#basic functions
print("len((1,2,3)) = " + str(len((1, 2, 3))))
print("(1, 2, 3) + (4, 5, 6) = " + str((1, 2, 3) + (4, 5, 6)))
print("('Hi! ',)*4 = " + str(('Hi! ',)*4))
print("3 in (1,2,3) = " + str(3 in (1,2,3)))

print("len((1,2,3)) = " + str(len((1,2,3))))
print("max((1,2,3)) = " + str(max((1,2,3))))
print("min((1,2,3)) = " + str(min((1,2,3))))
print("sum((1,2,3)) = " + str(sum((1,2,3))))


for x in (1, 2, 3): 
    print(x, end = ' ')



print("""
#########  Multi dimenstion tuples
""")

mult_tuple_2d_2 = ((1,2,3), (4,5), (6))
print(mult_tuple_2d_2)
print("len(mult_tuple_2d_2) -> ",len(mult_tuple_2d_2), "len(mult_tuple_2d_2[1]) -> ", len(mult_tuple_2d_2[1])) 