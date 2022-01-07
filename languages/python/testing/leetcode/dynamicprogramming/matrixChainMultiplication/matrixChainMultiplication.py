#!/usr/bin/env python3

import sys

class Solution:
    def matrixChainMultiplication(self, arr):                    
        return self.mc(arr, 1, len(arr)-1)

    def mc(self, arr, start, end):
        if start == end:
            return 0
        
        min_count = sys.maxsize
        for i in range(start, end):
            oper_count = self.mc(arr, start,i) + arr[start-1]*arr[i]*arr[end] + self.mc(arr, i+1, end)
            min_count = min(min_count, oper_count)

        return min_count


class SolutionMemoised:
    def matrixChainMultiplication(self, arr):
        memo = {}
        return self.mc(arr, 1, len(arr)-1, memo)

    def mc(self, arr, start, end, memo):
        if start == end:
            return 0
        
        if (start,end) in memo:
            return memo[(start,end)]

        min_count = sys.maxsize
        for i in range(start, end):
            oper_count = self.mc(arr, start,i, memo) + arr[start-1]*arr[i]*arr[end] + self.mc(arr, i+1, end, memo)
            min_count = min(min_count, oper_count)

        memo[(start, end)] = min_count
        return min_count

    

        
test = Solution()
print(test.matrixChainMultiplication([2,3,5,4]))
print(test.matrixChainMultiplication([10,30,5,60]))
print(test.matrixChainMultiplication([10,30,5,60,45,67,80,90,12,3,4,5,6]))
#print(test.matrixChainMultiplication([5]*100)) #will not work. Need dynamic programming

test = SolutionMemoised()
print(test.matrixChainMultiplication([2,3,5,4]))
print(test.matrixChainMultiplication([10,30,5,60]))
print(test.matrixChainMultiplication([10,30,5,60,45,67,80,90,12,3,4,5,6]))
print(test.matrixChainMultiplication([5]*100))

