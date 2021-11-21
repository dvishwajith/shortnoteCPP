#!/usr/bin/python3


class Solution:
    len_g = 0
    even_g = 0
    index_g = 0
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        index = n//2
        while index >= 0:
            res = self.expandAroundN(s, index)
            palin_len , even = res
            if palin_len + even > self.len_g :
                self.len_g = palin_len
                self.even_g = even
                self.index_g = index 
            index = index - 1

        index = n//2
        while index < n-1:
            res = self.expandAroundN(s, index)
            palin_len , even = res
            if palin_len + even > self.len_g :
                self.len_g = palin_len
                self.even_g = even
                self.index_g = index 
            index = index + 1

        return s[self.index_g - self.len_g + 1: self.index_g + self.len_g + self.even_g]
        
        
    def expandAroundN(self, s, n):
        i = 0
        evenofffset = 0
        evencomparison = False
        normalcomparison = True
        if n+1 < len(s) and s[n] == s[n+1]:
            evenofffset = 1
            evencomparison = True
        inc = 1
        while (n-i)>=0 and (n+i < len(s)) and inc > 0:
            inc = 0
            if normalcomparison and (s[n-i] == s[n+i]):
                inc = 1
            else:
                normalcomparison = False 

            if evencomparison and (n+i + evenofffset < len(s)) and (s[n-i] == s[n+i + evenofffset]):
                inc = 1
            else:
                evencomparison = False
                evenofffset = 0
            i = i + inc
        
        return i, evenofffset


sol = Solution()
res = sol.longestPalindrome("weqdccccdwer")
print(res)



