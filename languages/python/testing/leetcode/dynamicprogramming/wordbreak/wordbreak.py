#!/usr/bin/env python3

import sys

class Solution:
    def wordbreak(self, worddict, word):                    
        return self.wb(worddict, word, 0, len(word))

    def wb(self, worddict, word, start, end):
        words = []
        if start == end:
            return [""]
        else:
            for i in range(start, end):
                firstpart = word[start:i+1]
                if firstpart in worddict:
                    rest_wb = self.wb(worddict, word, i+1, end)
                    if len(rest_wb) != 0:
                        for second_part in rest_wb:
                            if second_part != '':
                                second_part = ' ' + second_part
                            
                            words.append(word[start:i+1] + second_part)

        return words


class SolutionMemoised:
    def wordbreak(self, worddict, word):
        memo = {}
        return self.wb(worddict, word, 0, len(word), memo)

    def wb(self, worddict, word, start, end, memo):
        words = []
        if start == end:
            return [""]
        elif start in memo:
            return memo[start]
        else:
            for i in range(start, end):
                firstpart = word[start:i+1]
                if firstpart in worddict:
                    rest_wb = self.wb(worddict, word, i+1, end, memo)
                    if len(rest_wb) != 0:
                        for second_part in rest_wb:
                            if second_part != '':
                                second_part = ' ' + second_part
                            
                            words.append(word[start:i+1] + second_part)

        memo[start] = words
        return words

        
test = Solution()
print(test.wordbreak({'a','bc','c','ab'}, 'abc'))
print(test.wordbreak({ 'this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'},'Wordbreakproblem'))


test = SolutionMemoised()
print(test.wordbreak({'a','bc','c','ab'}, 'abc'))
print(test.wordbreak({ 'this', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r', 'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'},'Wordbreakproblem'))