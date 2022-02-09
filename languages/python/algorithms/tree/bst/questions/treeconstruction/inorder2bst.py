#!/usr/bin/env python3

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def toBST(nums, start, end):
            if start > end:
                return None
            mid = (start + end)//2
            node = TreeNode(nums[mid], toBST(nums, start, mid-1), toBST(nums, mid+1, end))
            return node
        return toBST(nums, 0, len(nums)-1)


######################################testing

testcases = [
    [-10,-3,0,5,9],
    [1,3],
    [1,2,3,4,5,6,7]
]

def traverseInOrder(node):
    if node.left:
        traverseInOrder(node.left)
    
    print(node.val, end=" ")

    if node.right:
        traverseInOrder(node.right)

for test in testcases:
    sol = Solution()
    rootsol = sol.sortedArrayToBST(test)
    traverseInOrder(rootsol)
    print()
