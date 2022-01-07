#!/usr/bin/env python3
# from typing import List

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp_subseq = [[[] for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         dp_len = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         for i in range(len(text1)):
#             dp_row = []
#             for j in range(len(text2)):
#                 if dp_len[i+1][j] > dp_len[i][j+1]:
#                     dp_subseq[i+1][j+1] = [*dp_subseq[i+1][j]]
#                     dp_len[i+1][j+1] = dp_len[i+1][j]
#                 else:
#                     dp_subseq[i+1][j+1] = [*dp_subseq[i][j+1]]
#                     dp_len[i+1][j+1] = dp_len[i][j+1]
                    
#                 if text1[i] == text2[j]:
#                     if dp_len[i+1][j] >  dp_len[i][j+1]:
#                         dp_subseq[i+1][j+1].append(text1[i])
#                         dp_len[i+1][j+1] += 1
        
#         return dp_len[len(text1)][len(text2)]

# test = Solution()
# print(test.longestCommonSubsequence("abcde", "ace"))


#!/usr/bin/env python3
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_subseq = [[[] for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        dp_len = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):     
                if text1[i] == text2[j]:
                    dp_subseq[i+1][j+1] = [*dp_subseq[i][j]]
                    dp_subseq[i+1][j+1].append(text1[i])
                    dp_len[i+1][j+1] = dp_len[i][j] + 1
                else:
                    if dp_len[i+1][j] > dp_len[i][j+1]:
                        dp_subseq[i+1][j+1] = [*dp_subseq[i+1][j]]
                        dp_len[i+1][j+1] = dp_len[i+1][j]
                    else:
                        dp_subseq[i+1][j+1] = [*dp_subseq[i][j+1]]
                        dp_len[i+1][j+1] = dp_len[i][j+1]

        return dp_len

    def longestCommonSubsequenceOptimisedMem(self, text1: str, text2: str) -> int:
        dp_len = [[0 for _ in range(len(text2)+1)] for _ in range(1)]
        for i in range(len(text1)):
            dp_len.append([0 for _ in range(len(text2)+1)])
            for j in range(len(text2)):
                #print("mid", dp_len)
                if text1[i] == text2[j]:
                    dp_len[1][j+1] = dp_len[0][j] + 1
                else:
                    if dp_len[1][j] > dp_len[0][j+1]:
                        dp_len[1][j+1] = dp_len[1][j]
                    else:
                        dp_len[1][j+1] = dp_len[0][j+1]
                #print("fin", dp_len)
            dp_len.pop(0)
        return dp_len

test = Solution()
print(test.longestCommonSubsequence("abcde", "ace"))

"bsbininm"
"jmjkbkjkv"

print(test.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))


print(test.longestCommonSubsequence("aaaaa", "aaa"))




print("Optimised memory")
print(test.longestCommonSubsequenceOptimisedMem("abcde", "ace"))

"bsbininm"
"jmjkbkjkv"

print(test.longestCommonSubsequenceOptimisedMem("bsbininm", "jmjkbkjkv"))


print(test.longestCommonSubsequenceOptimisedMem("aaaaa", "aaa"))