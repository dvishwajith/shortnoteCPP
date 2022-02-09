#!/usr/bin/env python3


from typing import List
from typing import Optional


# Rhis is wrong

# class Solution:
#     def combinations(self, nums: List[int]) -> List[List[int]]:
#         def combinations_help(nums):
#             if not nums:
#                 return [[]]
#             else:
#                 combinations_list = [[]]
#                 for i in range(len(nums)):
#                     val = nums.pop(i)
#                     for pemrutation in combinations_help(nums):
#                         combinations_list.append([val] + pemrutation)
#                     nums.insert(i, val)
#                 return combinations_list
            
#         return combinations_help(nums)
    

# testcases = [
#     [1,2,3]
# ]
    

# for test in testcases:
#     sol = Solution()
#     answer = sol.combinations(test)
#     print(answer)
    
