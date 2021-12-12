#!/usr/bin/env python3


print(
'''
Map Example
'''    
)

fruit = ["apple", "banana", "pears", "appricot", "prange"]

fruits_start_with_a_MAP_OBJECT = map(lambda x: x[0] == 'a' , fruit)

fruits_start_with_a_list = list(fruits_start_with_a_MAP_OBJECT)
print("fruits_start_with_a_list ",  fruits_start_with_a_list)


print(
'''
Map Example 2
'''    
)

numbers = [1,2,3,4,5,6]
numbers2 = [1,2,3,4,5,6]

add_map_object = map(lambda x,y: x+y, numbers, numbers)
add_map_list = list(add_map_object)
print("add_map_list ", add_map_list)


print(
'''
Filter Example
'''    
)

numbers_lss_than_3_filter = filter(lambda x: x<3, numbers)
numbers_less_than_3 = list(numbers_lss_than_3_filter)
print("numbers_less_than_3 ", numbers_less_than_3)


print(
'''
reduce Example
You need to import functools for this

import functools
'''    
)

import functools

reduce_numbers = functools.reduce(lambda x ,y: x*y, numbers)
print("reduce_numbers ", reduce_numbers)