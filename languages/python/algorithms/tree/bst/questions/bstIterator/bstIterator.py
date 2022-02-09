from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # append root, plus all the left nodes
        self.addUntilNone(root)
    
    #add left node until no left node is there to add
    def addUntilNone(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        traversed_node = self.stack.pop()
        # add the right node of the popped node. ( This is the previous left most node)
        self.addUntilNone(traversed_node.right)
        return traversed_node.val
        
    # if stack is empty there are no nodes left
    def hasNext(self) -> bool:
        return self.stack           
            