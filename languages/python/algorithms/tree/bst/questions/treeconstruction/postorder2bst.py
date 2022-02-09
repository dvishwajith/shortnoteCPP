#!/usr/bin/env python3

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def psotorderToBst(self, nums: List[int]) -> Optional[TreeNode]:
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
        for num in nums[::-1]: # Just insert normally But from the end of the array
            root = insert(root, num)
        return root


######################################testing

testcases = [
    [7, 5, 1, 50, 40, 10]
]

def traverseInOrder(node):
    if node.left:
        traverseInOrder(node.left)
    
    print(node.val, end=" ")

    if node.right:
        traverseInOrder(node.right)

def traversePostOrder(node):
    if node.left:
        traversePostOrder(node.left)
    if node.right:
        traversePostOrder(node.right)
    print(node.val, end=" ")        

for test in testcases:
    sol = Solution()
    rootsol = sol.psotorderToBst(test)
    traverseInOrder(rootsol)
    print()
