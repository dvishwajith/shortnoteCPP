#!/usr/bin/env python3

from typing import List

class Solution:
    def subsetsumwrapper(self, d, arr):                    
        return self.subsetsum(d, arr, 0 , len(arr))

    def subsetsum(self, d, arr, start, end):
        if d == 0:
            return True
        if d < 0:
            return False
        elif start == end:
            return False
        else:
            return self.subsetsum(d-arr[start],arr, start+1,end) or self.subsetsum(d, arr, start+1, end)

    

class SolutionMemoised:
    def subsetsumwrapper(self, d, arr):
        memo = {}           
        return self.subsetsum(d, arr, 0 , len(arr), memo)

    def subsetsum(self, d, arr, start, end, memo):
        if d == 0:
            return True
        if d < 0:
            return False
        elif start == end:
            return False
        elif (d,start) in memo:
            return memo[(d,start)]
        else:
            val = self.subsetsum(d-arr[start],arr, start+1,end, memo) or self.subsetsum(d, arr, start+1, end, memo)
            memo[(d,start)] = val
            return val

class SolutionTabulation:
    def subsetsumwrapper(self, d, arr):
        dp = [[False for _ in range(len(arr)+1)] for _ in range(d+1)]
        dp[0][0] = True # sum value 0 is attainable even without any values in the array

        for i in range(0,d+1):
            for j in range(1,len(arr)+1):
                if dp[i][j-1] == True:
                    dp[i][j] = True
                else:
                    val = i - arr[j-1]
                    if val >= 0:
                        dp[i][j] = dp[val][j-1]

            
        #print(dp)
        return dp[-1][-1]

    

        
test = Solution()
print(test.subsetsumwrapper(5,[1,2,1,1]))

print(test.subsetsumwrapper(100,[1,2,1,1,4,7,8,2,4,6,5,1,3,5,6,9,9,12,3,5,6]))
#print(test.subsetsumwrapper(20, [1]*19))


test = SolutionMemoised()
print(test.subsetsumwrapper(5,[1,2,1,1]))

print(test.subsetsumwrapper(100,[1,2,1,1,4,7,8,2,4,6,5,1,3,5,6,9,9,12,3,5,6]))
print(test.subsetsumwrapper(501, [1]*500)) #cannot do this without memoised. Too much operations


test = SolutionTabulation()
print(test.subsetsumwrapper(5,[1,2,1,1]))

print(test.subsetsumwrapper(100,[1,2,1,1,4,7,8,2,4,6,5,1,3,5,6,9,9,12,3,5,6]))
print(test.subsetsumwrapper(3, [1]*2)) #cannot do this without memoised. Too much operations
print(test.subsetsumwrapper(100010, [1]*1000)) #cannot do this without memoised. Too much operations