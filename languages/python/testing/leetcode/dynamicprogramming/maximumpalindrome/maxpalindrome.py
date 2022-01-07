#!/usr/bin/env python3

import sys

class Solution:
    def maxpalindrome(self, str):                    
        return self.mp(str, 0, len(str))[0]

    def mp(self, str, start, end):
        if end - start <= 1:
            return str[start:end], True
        else:
            child_palindrome = ''
            if str[start] == str[end-1]:
                child_palindrome, check = self.mp(str,start+1, end-1)
                if check:
                    return str[start]+child_palindrome+str[start], True

            child_l, _ = self.mp(str,start, end-1)
            child_r, _ = self.mp(str,start+1, end)
            return max(child_palindrome, child_l, child_r, key=len), False

class SolutionMemoised:
    def maxpalindrome(self, str): 
        memo = {}                   
        return self.mp(str, 0, len(str), memo)[0]

    def mp(self, str, start, end, memo):
        if end - start <= 1:
            return str[start:end], True
        elif (start,end) in memo:
            return memo[(start,end)]
        else:
            child_palindrome = ''
            if str[start] == str[end-1]:
                child_palindrome, check = self.mp(str,start+1, end-1, memo)
                if check:
                    return str[start]+child_palindrome+str[start], True

            child_l, _ = self.mp(str,start, end-1, memo)
            child_r, _ = self.mp(str,start+1, end, memo)
            result = max(child_palindrome, child_l, child_r, key=len), False
            memo[(start,end)] = result
            return result


class SolutionTabular:
    def maxpalindrome(self, text): 
        length = len(text)
        dp_check = [[0 for _ in range(length)] for _ in range(length)]
        dp_palindrome = [['' for _ in range(length)] for _ in range(length)]
        
        #print(dp_check, dp_palindrome)

        for i in range(length):
            for j in range(i, -1, -1):
                if i == j:
                    dp_check[i][j] = 1
                    dp_palindrome[i][j] = text[i]
                elif text[i] == text[j]:
                    temp_pal_prev = max(dp_palindrome[i][j+1],dp_palindrome[i-1][j], key=len)
                    temp_pal = ''
                    if dp_check[i-1][j+1] != 0:
                        temp_pal = max(temp_pal, text[i]+dp_palindrome[i-1][j+1]+text[i], key=len)
                        
                    if dp_check[i][j+1] == 1 and dp_palindrome[i][j+1] == text[i]:
                        temp_pal = max(temp_pal, text[i]+dp_palindrome[i][j+1], key=len) 

                    if dp_check[i-1][j] == 1 and dp_palindrome[i-1][j] == text[i]:
                        temp_pal = max(temp_pal, text[i]+dp_palindrome[i-1][j], key=len)

                    if len(temp_pal) >= len(temp_pal_prev):
                        dp_check[i][j] = len(temp_pal)  
                        dp_palindrome[i][j] = temp_pal
                        #print(dp_check[i][j], len(temp_pal), dp_palindrome[i][j])
                    else:
                        dp_palindrome[i][j] = temp_pal_prev

                else:
                    dp_palindrome[i][j] = max(dp_palindrome[i-1][j], dp_palindrome[i][j+1], text[i], key=len)
                #print(dp_check, dp_palindrome)
        return dp_palindrome[length-1][0]

class SolutionTabularOptimised:
    def maxpalindrome(self, text): 
        length = len(text)
        dp = [[False for _ in range(length)] for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

        longest_palin = text[0:1]
        #print(dp_check, dp_palindrome)

        for i in range(1,length):
            for j in range(i-1, -1, -1):
                if text[i] == text[j]:
                    if i-j == 1 or dp[i-1][j+1] == True:
                        dp[i][j] = True
                        longest_palin = max(longest_palin,text[j:i+1], key=len)

        return longest_palin


test = Solution()
print(test.maxpalindrome('babad'))
print(test.maxpalindrome('cbbd'))

print("**memoised")
test = SolutionMemoised()
print(test.maxpalindrome('babad'))
print(test.maxpalindrome('cbbd'))
print(test.maxpalindrome("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni"))


print("****Tabularised")
test = SolutionTabular()
print(test.maxpalindrome('aaaa'))
print(test.maxpalindrome('cbbd'))
print(test.maxpalindrome("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni"))
print(test.maxpalindrome("aacabdkacaa"))


print("****TabularisedOptimised")
test = SolutionTabularOptimised()
print(test.maxpalindrome('aaaa'))
print(test.maxpalindrome('cbbd'))
print(test.maxpalindrome("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni"))
print(test.maxpalindrome("aacabdkacaa"))