# Definition for a binary tree node.

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.val = -1
        self.k = k
        self.inorder(root)
        return self.val
        #return self.inorderUsingStack(root,k)

    #using recursion    
    def inorder(self, node):
        if self.count >= self.k: # escape traversing after found
            return
        
        if node.left:
            self.inorder(node.left)

        self.count += 1    
        if self.count == self.k:
            self.val = node.val
            return              # escape traversing after found
        
        if node.right:
            self.inorder(node.right)

    # using stack and a while loops 
    def inorderUsingStack(self, node, k):
        stack = []
        stack.append(node)
        inorder_count = 0
        pointer_node = stack[0]
        
        while pointer_node is not None and stack:
            if pointer_node.left:
                stack.append(pointer_node.left)
                pointer_node = pointer_node.left
            else:
                traversed_node = stack.pop()
                
                inorder_count += 1
                if inorder_count == k:
                    return  traversed_node.val
                
                if traversed_node.right:
                    stack.append(traversed_node.right)
                    pointer_node = traversed_node.right
        return -1


    # Simpler way using stack and a while loops 
    def inorderUsingStack2ndway(self, root, k):
        stack = []
        node = root
        inorder_count = 0
        # add root and all the left most nodes to root
        while node:
            stack.append(node)
            node = node.left
        
        # untile stack is empty 
        while stack:
            traversed_node = stack.pop()        #pop a node fom the stack
            inorder_count +=1
            if inorder_count == k:
                return traversed_node.val

            node = traversed_node.right         # add it right node to the stack
            while node:                         # contine adding left most nodes of that right node untile there is none
                stack.append(node)
                node = node.left

        return -1



        
        