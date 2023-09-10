#!/usr/bin/env python3


from typing import List, ParamSpecArgs
from typing import Optional

class Solution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtracking(nums, subset=[])
        return self.result
    
    def backtracking(self, arr, subset):
        if not arr:
            self.result.append(subset)
        else:
            for i in range(len(arr)):
                val = arr.pop(i)
                subset.append(val)
                self.backtracking(arr, subset[:])
                arr.insert(i, val)
                subset.pop()

# second method Not optimised

class Solution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        ParamSpecArgs    

    


testcases = [
    [1,2,3]
]
    

for test in testcases:
    sol = Solution()
    answer = sol.subset(test)
    print(answer)


    
