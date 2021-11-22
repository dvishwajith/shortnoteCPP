#!/usr/bin/env python3

old_list = ['a', [1,2,3], ['b', 'c'], 5.5]

just_a_label_copy = old_list

print("old_list ", old_list)
print("just_a_label_copy ", just_a_label_copy)

just_a_label_copy[0] = 'Changed'

print("just_a_label_copy[0] = 'Changed'")
print("old_list ", old_list)


#As you can see = assing it to just a new label. 


import copy

print(
"""
##########shallow copy################

shallow_copied_list = copy.copy(old_list)
shallow_copied_list.append("Appended_this_string")
""")

shallow_copied_list = copy.copy(old_list)

#shallow copy will create a new copy . But nested objects/items will still has ame reference
shallow_copied_list.append("Appended_this_string")



print("old_list ", old_list)
print("shallow_copied_list ", shallow_copied_list)

shallow_copied_list[1][1] = 'a'
print("shallow_copied_list[1][1] = 'a'")
print("old_list ", old_list)

shallow_copied_list[0] = 'changedWithShallowCopy'

print("when shallow_copied_list[0] = 'changedWithShallowCopy'")
print("But old_list ", old_list)
print("This is becuse shallow_copied_list[0] = 'changedWithShallowCopy' replaced the whole object")



print(
"""
##########deep copy################

deep_copied_list = copy.deepcopy(old_list)
deep_copied_list.append("Appended_this_string")
""")

deep_copied_list = copy.deepcopy(old_list)
deep_copied_list[1][1] = 'b'
print("deep_copied_list[1][1] = 'b'")
print("old list nested objects does not chenge because of deepCopy old_list ", old_list)

