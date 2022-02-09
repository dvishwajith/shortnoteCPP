#!/usr/bin/env python3

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderToBst(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(node, val):
            if node is None:
                return TreeNode(val)
            else:
                if val < node.val:
                    node.left = insert(node.left, val)
                else:
                    node.right = insert(node.right, val)
                return node
        root = None
        for num in nums:
            root = insert(root, num)
        return root


######################################testing

testcases = [
    [10,1,5,7,40,50]
]

def traverseInOrder(node):
    if node.left:
        traverseInOrder(node.left)
    
    print(node.val, end=" ")

    if node.right:
        traverseInOrder(node.right)

for test in testcases:
    sol = Solution()
    rootsol = sol.preorderToBst(test)
    traverseInOrder(rootsol)
    print()
