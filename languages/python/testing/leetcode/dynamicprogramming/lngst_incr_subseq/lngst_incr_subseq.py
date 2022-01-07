
#!/usr/bin/env python3
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            print(i,dp[i])
                    
        return max(dp)
        
test = Solution()
print(test.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

