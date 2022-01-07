#!/usr/bin/env python3
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) > 0:
            #return self.checksumMemoized(0, len(nums)-1, nums)[0]
            return self.checksumOptimum(nums)
        else:
            return 0
          
    def checksum(self, start, end, arr):
        if start == end:
            return arr[start], arr[start]
        else:
            maxrsum, rsum = self.checksum(start+1, end, arr)
            maxlsum, lsum = self.checksum(start, end-1, arr)
            wholesum = rsum + arr[start]
            return max(maxrsum, maxlsum, wholesum), wholesum
            
    #memoized
    def checksumMemoized(self, start, end, arr, memo=None):
        if memo is None:
            memo = {}
        if start == end:
            return arr[start], arr[start]
        elif (start,end) in memo:
            return memo[(start,end)]
        else:
            maxrsum, rsum = self.checksumMemoized(start+1, end, arr, memo)
            maxlsum, lsum = self.checksumMemoized(start, end-1, arr, memo)
            wholesum = rsum + arr[start]
            retval = max(maxrsum, maxlsum, wholesum), wholesum
            memo[(start,end)] = retval
            return retval
    
    def checksumOptimum(self, nums):
        sum = -10**4 -1
        max = -10**4 -1
        for num in nums:
            if sum + num > num:
                sum = sum + num
            else:
                sum = num
                
            if sum > max:
                max = sum
        return max
                
        
        
# class Solution:
#     def maxSubArray(self, nums):
#         pre, suf = [*nums], [*nums]
#         for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
#         for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
#         def maxSubArray(A, L, R):
#             if L == R: return A[L]
#             mid = (L + R) // 2
#             return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
#         return maxSubArray(nums, 0, len(nums)-1)



test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))