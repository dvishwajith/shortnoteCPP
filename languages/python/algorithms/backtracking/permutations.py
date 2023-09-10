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

# second method Not optimised

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        track_permute_list = []
        
        self.backtrack(nums, track_permute_list)
        return self.result

    def backtrack(self, nums: List[int], track_permute_list: List[int]):
        if len(nums) == len(track_permute_list):
            self.result.append(track_permute_list[:])
            return

        for num in nums:
            if num not in track_permute_list:
                track_permute_list.append(num)
                self.backtrack(nums, track_permute_list)
                track_permute_list.pop()

class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums: List[int], index):
        if len(nums) <= index + 1:
            self.result.append(nums[:])
        else:
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                self.backtrack(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]


testcases = [
    [1,2,3]
]
    

for test in testcases:
    sol = Solution()
    answer = sol.permute(test)
    print(answer)

for test in testcases:
    sol = Solution2()
    answer = sol.permute(test)
    print(answer)  


for test in testcases:
    sol = Solution3()
    answer = sol.permute(test)
    print(answer)    
    


