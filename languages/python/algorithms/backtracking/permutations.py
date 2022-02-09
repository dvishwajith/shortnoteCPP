#!/usr/bin/env python3


from typing import List
from typing import Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_help(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            else:
                permute_list = []
                for i in range(len(nums)):
                    val = nums.pop(i)
                    for pemrutation in permute_help(nums):
                        permute_list.append([val] + pemrutation)
                    nums.insert(i, val)
                return permute_list
            
        return permute_help(nums)
    

testcases = [
    [1,2,3]
]
    

for test in testcases:
    sol = Solution()
    answer = sol.permute(test)
    print(answer)
    
